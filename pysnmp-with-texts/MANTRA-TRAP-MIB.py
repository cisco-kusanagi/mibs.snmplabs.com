#
# PySNMP MIB module MANTRA-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MANTRA-TRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:09:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
unknownDeviceTrapContents, domain, newFile, oldFile, file, myPort, deviceType, myHost, matePort, name, sbProducerPort, snName, result, runStatus, mateHost, minutes, devName, port, pepName, reason, group, host, sbProducerHost = mibBuilder.importSymbols("AGGREGATED-EXT-MIB", "unknownDeviceTrapContents", "domain", "newFile", "oldFile", "file", "myPort", "deviceType", "myHost", "matePort", "name", "sbProducerPort", "snName", "result", "runStatus", "mateHost", "minutes", "devName", "port", "pepName", "reason", "group", "host", "sbProducerHost")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ModuleIdentity, Counter32, MibIdentifier, Integer32, iso, NotificationType, snmpModules, ObjectIdentity, Bits, Gauge32, ObjectName, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "Counter32", "MibIdentifier", "Integer32", "iso", "NotificationType", "snmpModules", "ObjectIdentity", "Bits", "Gauge32", "ObjectName", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "enterprises")
TextualConvention, TruthValue, DisplayString, RowStatus, TimeStamp, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "RowStatus", "TimeStamp", "TestAndIncr")
lucent = MibIdentifier((1, 3, 6, 1, 4, 1, 1751))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1))
softSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198))
mantraTraps = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0))
if mibBuilder.loadTexts: mantraTraps.setLastUpdated('240701')
if mibBuilder.loadTexts: mantraTraps.setOrganization('Lucent Technologies')
if mibBuilder.loadTexts: mantraTraps.setContactInfo('')
if mibBuilder.loadTexts: mantraTraps.setDescription('The MIB module for entities implementing the xxxx protocol.')
lssProcessUnstartable = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 0)).setObjects(("AGGREGATED-EXT-MIB", "deviceType"), ("AGGREGATED-EXT-MIB", "domain"), ("AGGREGATED-EXT-MIB", "group"), ("AGGREGATED-EXT-MIB", "name"), ("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "port"), ("AGGREGATED-EXT-MIB", "runStatus"))
if mibBuilder.loadTexts: lssProcessUnstartable.setStatus('current')
if mibBuilder.loadTexts: lssProcessUnstartable.setDescription('Indicates a certain domain:group:process cannot be started even after several attempts. Variables are: 1) deviceType - this is either CC, H323, SS7 or EBGen (the various modules in SARAS) 2-4) domain:group:name - these three variables comprise the fully qualified name of the process (for start/ stop snmp-commands) 5) host - the hostname on which this process was to be run. 6) port - the port on which this process was exposing its health information. 7) runStatus - the current run-state in which the process is (likely to be 1). See moduleSummary for more explanation of runStatus. Severity: CRITICAL')
lssProcessCreated = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 1)).setObjects(("AGGREGATED-EXT-MIB", "deviceType"), ("AGGREGATED-EXT-MIB", "domain"), ("AGGREGATED-EXT-MIB", "group"), ("AGGREGATED-EXT-MIB", "name"), ("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "port"), ("AGGREGATED-EXT-MIB", "runStatus"))
if mibBuilder.loadTexts: lssProcessCreated.setStatus('current')
if mibBuilder.loadTexts: lssProcessCreated.setDescription('Indicates a certain domain:group:process was successfully created/re-started. Variables are same as the above trap: 1) deviceType - this is either CC, H323, SS7 or EBGen (the various modules in SARAS) 2-4) domain:group:name - these three variables comprise the fully qualified name of the process (for start/ stop snmp-commands) 5) host - the hostname on which this process was to be run. 6) port - the port on which this process was exposing its health information. 7) runStatus - the current run-state in which the process is. See moduleSummary for more explanation of runStatus. Severity: INFO')
lssProcessDied = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 2)).setObjects(("AGGREGATED-EXT-MIB", "deviceType"), ("AGGREGATED-EXT-MIB", "domain"), ("AGGREGATED-EXT-MIB", "group"), ("AGGREGATED-EXT-MIB", "name"), ("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "port"), ("AGGREGATED-EXT-MIB", "runStatus"))
if mibBuilder.loadTexts: lssProcessDied.setStatus('current')
if mibBuilder.loadTexts: lssProcessDied.setDescription('Indicates a certain domain:group:process died. 1) deviceType - this is either CC, H323, SS7 or EBGen (the various modules in SARAS) 2-4) domain:group:name - these three variables comprise the fully qualified name of the process (for start/ stop snmp-commands) 5) host - the hostname on which this process was to be run. 6) port - the port on which this process was exposing its health information. 7) runStatus - the current run-state in which the process is. See moduleSummary for more explanation of runStatus. Severity: MAJOR')
lssProcessKilled = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 3)).setObjects(("AGGREGATED-EXT-MIB", "deviceType"), ("AGGREGATED-EXT-MIB", "domain"), ("AGGREGATED-EXT-MIB", "group"), ("AGGREGATED-EXT-MIB", "name"), ("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "port"), ("AGGREGATED-EXT-MIB", "runStatus"))
if mibBuilder.loadTexts: lssProcessKilled.setStatus('current')
if mibBuilder.loadTexts: lssProcessKilled.setDescription('Indicates a certain domain:group:process was taken down manually in response to an snmp-set on mantraReboot, or processStop variable. Variables are exactly same as in the processDied trap: 1) deviceType - this is either CC, H323, SS7 or EBGen (the various modules in SARAS) 2-4) domain:group:name - these three variables comprise the fully qualified name of the process (for start/ stop snmp-commands) 5) host - the hostname on which this process was to be run. 6) port - the port on which this process was exposing its health information. 7) runStatus - the current run-state in which the process is. See moduleSummary for more explanation of runStatus. Severity: MAJOR')
lssProcessStateChange = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 4)).setObjects(("AGGREGATED-EXT-MIB", "deviceType"), ("AGGREGATED-EXT-MIB", "domain"), ("AGGREGATED-EXT-MIB", "group"), ("AGGREGATED-EXT-MIB", "name"), ("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "port"), ("AGGREGATED-EXT-MIB", "runStatus"))
if mibBuilder.loadTexts: lssProcessStateChange.setStatus('current')
if mibBuilder.loadTexts: lssProcessStateChange.setDescription('Indicates a change of status in a process. Usually sent to indicate if a process that was inactive, took over for an earlier active process that died. Variables are exactly same as all other traps: 1) deviceType - this is either CC, H323, SS7 or EBGen (the various modules in SARAS) 2-4) domain:group:name - these three variables comprise the fully qualified name of the process (for start/ stop snmp-commands) 5) host - the hostname on which this process was to be run. 6) port - the port on which this process was exposing its health information. 7) runStatus - the current run-state in which the process is. See moduleSummary for more explanation of runStatus. Severity: MAJOR')
lssInternalError = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 5)).setObjects(("AGGREGATED-EXT-MIB", "unknownDeviceTrapContents"))
if mibBuilder.loadTexts: lssInternalError.setStatus('current')
if mibBuilder.loadTexts: lssInternalError.setDescription('An event is sent up as lssInternalError, if there is an error in formatting, and event construction does not succeed. The variables are: 1) unknownDeviceTrapContents - a string representing the event text as the pep received it. Severity: MAJOR')
lssElementSuccessfulConnection = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 6)).setObjects(("AGGREGATED-EXT-MIB", "pepName"), ("AGGREGATED-EXT-MIB", "devName"), ("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "port"), ("AGGREGATED-EXT-MIB", "file"))
if mibBuilder.loadTexts: lssElementSuccessfulConnection.setStatus('current')
if mibBuilder.loadTexts: lssElementSuccessfulConnection.setDescription('Indicates that the pep was sucessfully able to connect to the source of events specified in its config. The variables are: 1) pepName - this is the name of the PEP who is raising the event 2) devName - this is the logical name of the device this pep is connected to 3-4) host:port - these two identify the device that was mounted by the pep 5) file - this is the file name used internally start-up event, mainly. Severity: INFO')
lssElementFileUnReadable = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 7)).setObjects(("AGGREGATED-EXT-MIB", "pepName"), ("AGGREGATED-EXT-MIB", "devName"), ("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "port"), ("AGGREGATED-EXT-MIB", "file"))
if mibBuilder.loadTexts: lssElementFileUnReadable.setStatus('current')
if mibBuilder.loadTexts: lssElementFileUnReadable.setDescription("Indicates that the pep's connection exists to the device, but the file named in the trap is not readable. The variables are: 1) pepName - this is the name of the PEP who is raising the event 2) devName - this is the logical name of the device this pep is connected to 3-4) host:port - these two identify the device that was mounted by the pep 5) file - this is the file name used internally Severity: MAJOR")
lssElementDisconnect = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 8)).setObjects(("AGGREGATED-EXT-MIB", "pepName"), ("AGGREGATED-EXT-MIB", "devName"), ("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "port"), ("AGGREGATED-EXT-MIB", "file"))
if mibBuilder.loadTexts: lssElementDisconnect.setStatus('current')
if mibBuilder.loadTexts: lssElementDisconnect.setDescription("Indicates that the pep's connection to the source of events was severed. This could either be because device process died, or because there is a network outage. The variables are: 1) pepName - this is the name of the PEP who is raising the event 2) devName - this is the logical name of the device this pep is connected to 3-4) host:port - these two identify the device that was mounted by the pep 5) file - this is the file name used internally Severity: MAJOR")
lssElementUnReachable = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 9)).setObjects(("AGGREGATED-EXT-MIB", "pepName"), ("AGGREGATED-EXT-MIB", "devName"), ("AGGREGATED-EXT-MIB", "host"), ("AGGREGATED-EXT-MIB", "port"), ("AGGREGATED-EXT-MIB", "file"), ("AGGREGATED-EXT-MIB", "minutes"))
if mibBuilder.loadTexts: lssElementUnReachable.setStatus('current')
if mibBuilder.loadTexts: lssElementUnReachable.setDescription("Indicates that the pep's connection to the device has not been up for some time now, indicated in minutes. The variables are: 1) pepName - this is the name of the PEP who is raising the event 2) devName - this is the logical name of the device this pep is connected to 3-4) host, port - these two identify the device that was mounted by the pep 5) file - this is the file name used internally minutes - the time in minutes for which the connection to the device has not been up. Severity: MAJOR")
logFileChanged = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 10)).setObjects(("AGGREGATED-EXT-MIB", "oldFile"), ("AGGREGATED-EXT-MIB", "newFile"), ("AGGREGATED-EXT-MIB", "result"), ("AGGREGATED-EXT-MIB", "reason"))
if mibBuilder.loadTexts: logFileChanged.setStatus('current')
if mibBuilder.loadTexts: logFileChanged.setDescription("Indicates that a log-file-change attempt is successful or failure. The variables are: 1) oldFile - this is the name of the old file which was to be changed. 2) newFile - this is the new log file name 3) result - this indicates 'success' or failure of logFileChange attempt. 4) reason - this describes the reason when log file change has failed. Severity: INFO")
lssFTMateConnect = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 11)).setObjects(("AGGREGATED-EXT-MIB", "snName"), ("AGGREGATED-EXT-MIB", "myHost"), ("AGGREGATED-EXT-MIB", "myPort"), ("AGGREGATED-EXT-MIB", "mateHost"), ("AGGREGATED-EXT-MIB", "matePort"))
if mibBuilder.loadTexts: lssFTMateConnect.setStatus('current')
if mibBuilder.loadTexts: lssFTMateConnect.setDescription('Indicates that this ServiceNode was sucessfully able to connect to its redundant mate. This event is usually raised by the Backup mate who is responsible for monitoring its respective Primary. The variables are: 1) snName - this is the name of the ServiceNode who is raising the event. 2-3) myHost:myPort - these identify the host and port of the ServiceNode raising the event. 4-5) mateHost:matePort - these identify the host and port of the mate to which this ServiceNode connected. Severity: INFO')
lssFTMateDisconnect = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 12)).setObjects(("AGGREGATED-EXT-MIB", "snName"), ("AGGREGATED-EXT-MIB", "myHost"), ("AGGREGATED-EXT-MIB", "myPort"), ("AGGREGATED-EXT-MIB", "mateHost"), ("AGGREGATED-EXT-MIB", "matePort"))
if mibBuilder.loadTexts: lssFTMateDisconnect.setStatus('current')
if mibBuilder.loadTexts: lssFTMateDisconnect.setDescription('Indicates that this ServiceNode has lost connection to its redundant mate due to either process or host failure. This event is usually raised by the Backup mate who is monitoring its respective Primary. Connection will be established upon recovery of the mate. The variables are: 1) snName - this is the name of the ServiceNode who is raising the event 2-3) myHost:myPort - these identify the host and port of the ServiceNode raising the event. 4-5) mateHost:matePort - these identify the host and port of the mate to which this ServiceNode lost connection. Severity: MAJOR')
sbProducerUnreachable = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 13)).setObjects(("AGGREGATED-EXT-MIB", "pepName"), ("AGGREGATED-EXT-MIB", "devName"), ("AGGREGATED-EXT-MIB", "sbProducerHost"), ("AGGREGATED-EXT-MIB", "sbProducerPort"))
if mibBuilder.loadTexts: sbProducerUnreachable.setStatus('current')
if mibBuilder.loadTexts: sbProducerUnreachable.setDescription('Indicates that this Socket Based Producer is not reachable by the Policy Enforcement Point. The variables are: 1) pepName - this is the name of the Policy Enforcement Point (PEP) who is raising the event 2) devName: Device which is unreachable 3) SBProducerHost: Host where the Socket Based event producer is on. 4) SBProducerPort: Port where the Socket Based event producer is running on. Severity: MAJOR')
sbProducerConnected = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 14)).setObjects(("AGGREGATED-EXT-MIB", "pepName"), ("AGGREGATED-EXT-MIB", "devName"), ("AGGREGATED-EXT-MIB", "sbProducerHost"), ("AGGREGATED-EXT-MIB", "sbProducerPort"))
if mibBuilder.loadTexts: sbProducerConnected.setStatus('current')
if mibBuilder.loadTexts: sbProducerConnected.setDescription('Indicates that this Socket Based Producer has connected to the Policy Enforcement Point (PEP). The variables are: 1) pepName - this is the name of the Policy Enforcement Point (PEP) who is raising the event 2) devName: Device which is unreachable 3) SBProducerHost: Host where the Socket Based event producer is on. 4) SBProducerPort: Port where the Socket Based event producer is running on. Severity: MAJOR')
sbProducerRegistered = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 15)).setObjects(("AGGREGATED-EXT-MIB", "pepName"), ("AGGREGATED-EXT-MIB", "devName"), ("AGGREGATED-EXT-MIB", "sbProducerHost"), ("AGGREGATED-EXT-MIB", "sbProducerPort"))
if mibBuilder.loadTexts: sbProducerRegistered.setStatus('current')
if mibBuilder.loadTexts: sbProducerRegistered.setDescription('Indicates that this Socket Based Producer has registered with the Policy Enforcement Point (PEP). The variables are: 1) pepName - this is the name of the Policy Enforcement Point (PEP) who is raising the event 2) devName: Device which is unreachable 3) SBProducerHost: Host where the Socket Based event producer is on. 4) SBProducerPort: Port where the Socket Based event producer is running on. Severity: INFO')
sbProducerDisconnected = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 16)).setObjects(("AGGREGATED-EXT-MIB", "pepName"), ("AGGREGATED-EXT-MIB", "devName"), ("AGGREGATED-EXT-MIB", "sbProducerHost"), ("AGGREGATED-EXT-MIB", "sbProducerPort"))
if mibBuilder.loadTexts: sbProducerDisconnected.setStatus('current')
if mibBuilder.loadTexts: sbProducerDisconnected.setDescription('Indicates that this Socket Based Producer has disconnected from the Policy Enforcement Point (PEP). The variables are: 1) pepName - this is the name of the Policy Enforcement Point (PEP) who is raising the event 2) devName: Device which is unreachable 3) SBProducerHost: Host where the Socket Based event producer is on. 4) SBProducerPort: Port where the Socket Based event producer is running on. Severity: INFO')
sbProducerCannotRegister = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 17)).setObjects(("AGGREGATED-EXT-MIB", "pepName"), ("AGGREGATED-EXT-MIB", "devName"), ("AGGREGATED-EXT-MIB", "sbProducerHost"), ("AGGREGATED-EXT-MIB", "sbProducerPort"))
if mibBuilder.loadTexts: sbProducerCannotRegister.setStatus('current')
if mibBuilder.loadTexts: sbProducerCannotRegister.setDescription('Indicates that this Socket Based Producer cannot register to the Policy Enforcement Point (PEP). The variables are: 1) pepName - this is the name of the Policy Enforcement Point (PEP) who is raising the event 2) devName: Device which is unreachable 3) SBProducerHost: Host where the Socket Based event producer is on. 4) SBProducerPort: Port where the Socket Based event producer is running on. Severity: INFO')
sbProducerCannotDisconnect = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 0, 18)).setObjects(("AGGREGATED-EXT-MIB", "pepName"), ("AGGREGATED-EXT-MIB", "devName"), ("AGGREGATED-EXT-MIB", "sbProducerHost"), ("AGGREGATED-EXT-MIB", "sbProducerPort"))
if mibBuilder.loadTexts: sbProducerCannotDisconnect.setStatus('current')
if mibBuilder.loadTexts: sbProducerCannotDisconnect.setDescription('Indicates that this Socket Based Producer cannot disconenct from the Policy Enforcement Point (PEP). The variables are: 1) pepName - this is the name of the Policy Enforcement Point (PEP) who is raising the event 2) devName: Device which is unreachable 3) SBProducerHost: Host where the Socket Based event producer is on. 4) SBProducerPort: Port where the Socket Based event producer is running on. Severity: INFO')
mibBuilder.exportSymbols("MANTRA-TRAP-MIB", mantraTraps=mantraTraps, lssElementUnReachable=lssElementUnReachable, sbProducerDisconnected=sbProducerDisconnected, lssElementFileUnReadable=lssElementFileUnReadable, PYSNMP_MODULE_ID=mantraTraps, sbProducerRegistered=sbProducerRegistered, sbProducerCannotDisconnect=sbProducerCannotDisconnect, logFileChanged=logFileChanged, lssFTMateDisconnect=lssFTMateDisconnect, lssProcessDied=lssProcessDied, lucent=lucent, lssProcessKilled=lssProcessKilled, lssInternalError=lssInternalError, lssProcessUnstartable=lssProcessUnstartable, sbProducerUnreachable=sbProducerUnreachable, lssProcessStateChange=lssProcessStateChange, lssFTMateConnect=lssFTMateConnect, softSwitch=softSwitch, lssProcessCreated=lssProcessCreated, sbProducerConnected=sbProducerConnected, products=products, lssElementDisconnect=lssElementDisconnect, lssElementSuccessfulConnection=lssElementSuccessfulConnection, sbProducerCannotRegister=sbProducerCannotRegister)
