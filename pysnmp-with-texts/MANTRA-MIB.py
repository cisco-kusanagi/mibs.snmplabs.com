#
# PySNMP MIB module MANTRA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MANTRA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:09:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
snmpModules, Counter32, iso, ObjectIdentity, MibIdentifier, enterprises, ModuleIdentity, ObjectName, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, Counter64, Integer32, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "snmpModules", "Counter32", "iso", "ObjectIdentity", "MibIdentifier", "enterprises", "ModuleIdentity", "ObjectName", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "Counter64", "Integer32", "NotificationType", "TimeTicks")
TextualConvention, RowStatus, TimeStamp, TestAndIncr, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TimeStamp", "TestAndIncr", "TruthValue", "DisplayString")
lucent = MibIdentifier((1, 3, 6, 1, 4, 1, 1751))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1))
softSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198))
mantraAdmin = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99))
if mibBuilder.loadTexts: mantraAdmin.setLastUpdated('310701')
if mibBuilder.loadTexts: mantraAdmin.setOrganization('Lucent Technologies')
if mibBuilder.loadTexts: mantraAdmin.setContactInfo('')
if mibBuilder.loadTexts: mantraAdmin.setDescription('The MIB module for entities implementing the xxxx protocol.')
moduleSummary = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleSummary.setStatus('current')
if mibBuilder.loadTexts: moduleSummary.setDescription('A short summary of the status of the mantra software modules. This is provided as a convenience variable to the administrator, so he can see everything at a glance without polling each component separately. Processes can be in one of the four states: 0 - not started, 1 - in the process of starting up, 2 - up, but inactive (only one process in a fail-over group is active at a time) 3 - up, and active 4 - died (on its own) 5 - stopped, i.e. by some command')
mantraUpTime = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mantraUpTime.setStatus('current')
if mibBuilder.loadTexts: mantraUpTime.setDescription('The time (in hundredths of a second) since the mantra software was last re-initialized.')
mantraRetryCount = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mantraRetryCount.setStatus('current')
if mibBuilder.loadTexts: mantraRetryCount.setDescription('The number of retry attempts to make when starting a software component managed by this mib.')
mantraRetryInterval = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mantraRetryInterval.setStatus('current')
if mibBuilder.loadTexts: mantraRetryInterval.setDescription('The time in seconds between the above retry attempts.')
mantraReboot = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mantraReboot.setStatus('current')
if mibBuilder.loadTexts: mantraReboot.setDescription('Each time the user executes a set on this entry with a value equal to 1, all components controlled by this module in the softswitch are rebooted.')
mantraTurnoff = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mantraTurnoff.setStatus('current')
if mibBuilder.loadTexts: mantraTurnoff.setDescription('Each time the user executes a set on this entry with a value equal to 1, all components controlled by this module in the softswitch are turned off.')
startProcess = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: startProcess.setStatus('current')
if mibBuilder.loadTexts: startProcess.setDescription('The user can set this entry to the name of the module that needs to be started, and it causes that process to be restarted. If the process is already running, no action takes place. The process name being set must be in the same format switch:group:pid, as returned in moduleSummary')
stopProcess = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stopProcess.setStatus('current')
if mibBuilder.loadTexts: stopProcess.setDescription('The user can set this entry to the name of the module that needs to be stopped, and it causes that process to be stopped. If the process is already stopped, no action takes place. The process name being set must be in the same format switch:group:pid, as returned in moduleSummary')
currentProcess = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: currentProcess.setStatus('current')
if mibBuilder.loadTexts: currentProcess.setDescription('The user can set this entry to the name of the process he wants to interact with, and all future gets on processState variable return the health information for that process')
processState = MibScalar((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 99, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: processState.setStatus('current')
if mibBuilder.loadTexts: processState.setDescription('A get on this variable returns the health of the process named in currentProcess variable.')
mibBuilder.exportSymbols("MANTRA-MIB", mantraAdmin=mantraAdmin, stopProcess=stopProcess, PYSNMP_MODULE_ID=mantraAdmin, softSwitch=softSwitch, mantraRetryCount=mantraRetryCount, mantraTurnoff=mantraTurnoff, processState=processState, startProcess=startProcess, lucent=lucent, mantraUpTime=mantraUpTime, mantraReboot=mantraReboot, currentProcess=currentProcess, mantraRetryInterval=mantraRetryInterval, moduleSummary=moduleSummary, products=products)
