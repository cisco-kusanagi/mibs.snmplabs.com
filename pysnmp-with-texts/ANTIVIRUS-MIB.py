#
# PySNMP MIB module ANTIVIRUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ANTIVIRUS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:22:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
naiTrapSeverity, naiTrapGMTTime, naiTrapAlarmSourceDNSName, naiTrapAlarmSourceAddress, naiTrapAgent, naiTrapLocalTime, naiTrapURL, naiTrapAgentVersion, naiTrapPseudoID, naiTrapDescription, nai = mibBuilder.importSymbols("NAI-MIB", "naiTrapSeverity", "naiTrapGMTTime", "naiTrapAlarmSourceDNSName", "naiTrapAlarmSourceAddress", "naiTrapAgent", "naiTrapLocalTime", "naiTrapURL", "naiTrapAgentVersion", "naiTrapPseudoID", "naiTrapDescription", "nai")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, iso, MibIdentifier, NotificationType, Gauge32, ObjectIdentity, TimeTicks, NotificationType, Bits, Unsigned32, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "MibIdentifier", "NotificationType", "Gauge32", "ObjectIdentity", "TimeTicks", "NotificationType", "Bits", "Unsigned32", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
naiAntiVirus = MibIdentifier((1, 3, 6, 1, 4, 1, 3401, 4))
naiAntiVirusTrapAgentUser = MibScalar((1, 3, 6, 1, 4, 1, 3401, 4, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naiAntiVirusTrapAgentUser.setStatus('mandatory')
if mibBuilder.loadTexts: naiAntiVirusTrapAgentUser.setDescription('This information identifies the user account which is causing the alarm.')
naiAntiVirusTrapInfectedFile = MibScalar((1, 3, 6, 1, 4, 1, 3401, 4, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naiAntiVirusTrapInfectedFile.setStatus('mandatory')
if mibBuilder.loadTexts: naiAntiVirusTrapInfectedFile.setDescription('This information idenifies the infected file which is causing the alarm.')
naiAntiVirusTrapVirusName = MibScalar((1, 3, 6, 1, 4, 1, 3401, 4, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naiAntiVirusTrapVirusName.setStatus('mandatory')
if mibBuilder.loadTexts: naiAntiVirusTrapVirusName.setDescription('This information identifies the virus which is causing the alarm.')
naiAntiVirusTrapTaskName = MibScalar((1, 3, 6, 1, 4, 1, 3401, 4, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naiAntiVirusTrapTaskName.setStatus('mandatory')
if mibBuilder.loadTexts: naiAntiVirusTrapTaskName.setDescription('This information identifies the task which generated the alarm.')
naiAntiVirusTrapStatus = MibScalar((1, 3, 6, 1, 4, 1, 3401, 4, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naiAntiVirusTrapStatus.setStatus('optional')
if mibBuilder.loadTexts: naiAntiVirusTrapStatus.setDescription('This information identifies the status of the file for which the trap is sent.')
naiAntiVirusTrapOS = MibScalar((1, 3, 6, 1, 4, 1, 3401, 4, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naiAntiVirusTrapOS.setStatus('mandatory')
if mibBuilder.loadTexts: naiAntiVirusTrapOS.setDescription('This information identifies the platform of the machine from which the trap is sent.')
naiAntiVirusTrapEngineVersion = MibScalar((1, 3, 6, 1, 4, 1, 3401, 4, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naiAntiVirusTrapEngineVersion.setStatus('mandatory')
if mibBuilder.loadTexts: naiAntiVirusTrapEngineVersion.setDescription('This information identifies the version of the Scan engine on the machine for which the trap is sent.')
naiAntiVirusTrapDATVersion = MibScalar((1, 3, 6, 1, 4, 1, 3401, 4, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: naiAntiVirusTrapDATVersion.setStatus('mandatory')
if mibBuilder.loadTexts: naiAntiVirusTrapDATVersion.setDescription('This information identifies the the version of the DAT files on the machine for which the trap is sent.')
naiAntiVirusTrap = NotificationType((1, 3, 6, 1, 4, 1, 3401, 4) + (0,1)).setObjects(("NAI-MIB", "naiTrapAgent"), ("NAI-MIB", "naiTrapAgentVersion"), ("NAI-MIB", "naiTrapSeverity"), ("NAI-MIB", "naiTrapDescription"), ("NAI-MIB", "naiTrapAlarmSourceAddress"), ("NAI-MIB", "naiTrapAlarmSourceDNSName"), ("NAI-MIB", "naiTrapGMTTime"), ("NAI-MIB", "naiTrapLocalTime"), ("NAI-MIB", "naiTrapURL"), ("NAI-MIB", "naiTrapPseudoID"), ("ANTIVIRUS-MIB", "naiAntiVirusTrapAgentUser"), ("ANTIVIRUS-MIB", "naiAntiVirusTrapInfectedFile"), ("ANTIVIRUS-MIB", "naiAntiVirusTrapVirusName"), ("ANTIVIRUS-MIB", "naiAntiVirusTrapTaskName"), ("ANTIVIRUS-MIB", "naiAntiVirusTrapStatus"), ("ANTIVIRUS-MIB", "naiAntiVirusTrapOS"), ("ANTIVIRUS-MIB", "naiAntiVirusTrapEngineVersion"), ("ANTIVIRUS-MIB", "naiAntiVirusTrapDATVersion"))
if mibBuilder.loadTexts: naiAntiVirusTrap.setDescription('The NAI AntiVirus alarm information.')
mibBuilder.exportSymbols("ANTIVIRUS-MIB", naiAntiVirus=naiAntiVirus, naiAntiVirusTrapInfectedFile=naiAntiVirusTrapInfectedFile, naiAntiVirusTrapOS=naiAntiVirusTrapOS, naiAntiVirusTrapDATVersion=naiAntiVirusTrapDATVersion, naiAntiVirusTrapVirusName=naiAntiVirusTrapVirusName, naiAntiVirusTrapEngineVersion=naiAntiVirusTrapEngineVersion, naiAntiVirusTrapTaskName=naiAntiVirusTrapTaskName, naiAntiVirusTrapStatus=naiAntiVirusTrapStatus, naiAntiVirusTrap=naiAntiVirusTrap, naiAntiVirusTrapAgentUser=naiAntiVirusTrapAgentUser)
