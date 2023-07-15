#!/bin/bash
# pre-commit.sh

# Initialize error flag
error=0
DIRECTORY="src"

PYLINT="Pylint"
MYPY="Mypy"
UNIT_TESTS="Unit tests"


echo "####################################################################################################"
echo "   _____ __        __  _         ______          __        ___                __           _     
  / ___// /_____ _/ /_(_)____   / ____/___  ____/ /__     /   |  ____  ____ _/ /_  _______(_)____
  \__ \/ __/ __ \`/ __/ / ___/  / /   / __ \/ __  / _ \   / /\ | / __ \/ __ \`/ / / / / ___/ / ___/
 ___/ / /_/ /_/ / /_/ / /__   / /___/ /_/ / /_/ /  __/  / ___ |/ / / / /_/ / / /_/ (__  ) (__  ) 
/____/\__/\__,_/\__/_/\___/   \____/\____/\__,_/\___/  /_/  |_/_/ /_/\__,_/_/\__, /____/_/____/  
                                                                            /____/               "
                                                                                                         
echo "\n###################################################################################################\n"

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

# Run unit tests
echo "🔎 [STEP 1] Running $UNIT_TESTS..."
python -m coverage run -m unittest && handle_success "$UNIT_TESTS" || handle_error $UNIT_TESTS
echo "--------------------------------------------------------------------\n"

# Run Pylint
echo "🔎 [STEP 2] Running $PYLINT..."
pylint main.py $DIRECTORY && handle_success "$PYLINT" || handle_error $PYLINT
echo "--------------------------------------------------------------------\n"

# Run Mypy
echo "🔎 [STEP 3] Running $MYPY...\n"
mypy main.py $DIRECTORY && handle_success "$MYPY" || handle_error $MYPY
echo "--------------------------------------------------------------------\n"

# Check error flag
if [ $error -eq 1 ]
then
    echo "🛑 Some checks failed. Commit aborted"
    exit 1
else
    echo "🎉 All checks passed! Commit successful"
fi
