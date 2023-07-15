#!/bin/bash
# pre-commit.sh

if [ "$1" = "-v" ]
then
    ENABLE_VERBOSE=true
else
    ENABLE_VERBOSE=false
fi

# Initialize error flag
error=0
DIRECTORY="src"

PYLINT="Pylint"
MYPY="Mypy"
UNIT_TESTS="Unit tests"

# Enable verbose mode

print_header () {
    echo "****************************************************************************************************"
    echo "     _____ __        __  _         ______          __        ___                __           _     
    / ___// /_____ _/ /_(_)____   / ____/___  ____/ /__     /   |  ____  ____ _/ /_  _______(_)____
    \__ \/ __/ __ \`/ __/ / ___/  / /   / __ \/ __  / _ \   / /\ | / __ \/ __ \`/ / / / / ___/ / ___/
   ___/ / /_/ /_/ / /_/ / /__   / /___/ /_/ / /_/ /  __/  / ___ |/ / / / /_/ / / /_/ (__  ) (__  ) 
  /____/\__/\__,_/\__/_/\___/   \____/\____/\__,_/\___/  /_/  |_/_/ /_/\__,_/_/\__, /____/_/____/  
                                                                              /____/               "
                                                                                                            
    echo "***************************************************************************************************"
    echo ""
}

# Function to handle failures
handle_error () {
    echo "❌ $1 failed"
    error=1
}

handle_success () {
    echo "✅ $1 passed"
}

show_coverage() {
    echo "\n🛡️ 🛡️ 🛡️ Coverage report 🛡️ 🛡️ 🛡️"
    python -m coverage report
    echo ""
}

print_step () {
    if [ $ENABLE_VERBOSE = true ]; then echo "[STEP $1] ⚜️ Running $2..."; fi
}

# Print header
if [ $ENABLE_VERBOSE = true ]; then print_header; fi

# Run unit tests
print_step 1 "$UNIT_TESTS"
python -m coverage run -m unittest && handle_success "$UNIT_TESTS" || handle_error $UNIT_TESTS
if [ $ENABLE_VERBOSE = true ]; then show_coverage; fi




# Run Pylint
echo "********************************************************************"
print_step 2 "$PYLINT"
pylint main.py $DIRECTORY && handle_success "$PYLINT" || handle_error $PYLINT
echo "********************************************************************"
echo ""

# Run Mypy
print_step 3 "$MYPY"
mypy main.py $DIRECTORY && handle_success "$MYPY" || handle_error $MYPY
echo "********************************************************************"

# Check error flag
if [ $error -eq 1 ]
then
    echo ""
    echo "🛑 Some checks failed. Commit aborted"
    exit 1
else
    echo ""
    echo "🎉 All checks passed! Commit successful"
fi
