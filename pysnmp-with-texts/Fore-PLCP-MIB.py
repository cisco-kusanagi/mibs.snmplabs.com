#
# PySNMP MIB module Fore-PLCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-PLCP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:17:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
asx, = mibBuilder.importSymbols("Fore-Common-MIB", "asx")
trapLogIndex, = mibBuilder.importSymbols("Fore-TrapLog-MIB", "trapLogIndex")
ifName, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifName", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, ModuleIdentity, NotificationType, iso, Counter64, ObjectIdentity, IpAddress, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "ModuleIdentity", "NotificationType", "iso", "Counter64", "ObjectIdentity", "IpAddress", "Gauge32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
forePlcpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13))
if mibBuilder.loadTexts: forePlcpMib.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: forePlcpMib.setOrganization('FORE')
if mibBuilder.loadTexts: forePlcpMib.setContactInfo(' Postal: FORE Systems Inc. 1000 FORE Drive Warrendale, PA 15086-7502 Tel: +1 724 742 6900 Email: nm_mibs@fore.com Web: http://www.fore.com')
if mibBuilder.loadTexts: forePlcpMib.setDescription(' This mib implements management information for the PLCP convergence layer in an atm interface. Typically PLCP framing is used to encapsulate ATM cells for transmission over a DS3/E3 link.')
forePlcpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 1), )
if mibBuilder.loadTexts: forePlcpConfigTable.setStatus('current')
if mibBuilder.loadTexts: forePlcpConfigTable.setDescription('A table of PLCP convergence layer information configuration parameters.')
forePlcpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: forePlcpConfigEntry.setStatus('current')
if mibBuilder.loadTexts: forePlcpConfigEntry.setDescription('A table entry containing PLCP convergence layer configuration information for each atm interface using PLCP.')
forePlcpConfigFrameFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("forePlcpFrameFormatDs1", 1), ("forePlcpFrameFormatE1", 2), ("forePlcpFrameFormatDs3", 3), ("forePlcpFrameFormatE3", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: forePlcpConfigFrameFormat.setStatus('current')
if mibBuilder.loadTexts: forePlcpConfigFrameFormat.setDescription('This variable controls the PLCP framing format used to carry ATM cells over this interface. Note that some interfaces may not support all formats and that this variable may be read-only for some interfaces.')
forePlcpTotalTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 2), )
if mibBuilder.loadTexts: forePlcpTotalTable.setStatus('current')
if mibBuilder.loadTexts: forePlcpTotalTable.setDescription('A table of PLCP convergence layer information and parameters.')
forePlcpTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: forePlcpTotalEntry.setStatus('current')
if mibBuilder.loadTexts: forePlcpTotalEntry.setDescription('A table entry containing PLCP convergence layer information for each atm interface using PLCP.')
forePlcpTotalFerrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forePlcpTotalFerrCount.setStatus('current')
if mibBuilder.loadTexts: forePlcpTotalFerrCount.setDescription('The number of framing errors detected since the interface was reset. A framing error is determined by errors in the A1 and A2 bytes of the PLCP frame.')
forePlcpTotalLofSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forePlcpTotalLofSeconds.setStatus('current')
if mibBuilder.loadTexts: forePlcpTotalLofSeconds.setDescription('The number of seconds an out of frame condition persisted.')
forePlcpTotalBip8Count = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forePlcpTotalBip8Count.setStatus('current')
if mibBuilder.loadTexts: forePlcpTotalBip8Count.setDescription('The number of Bit Interleaved Parity errors detected since the interface was reset. A BIP error is determined by using the parity carried in the B1 byte of the PLCP frame.')
forePlcpTotalFebeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forePlcpTotalFebeCount.setStatus('current')
if mibBuilder.loadTexts: forePlcpTotalFebeCount.setDescription('The number of Far End BIP Errors detected. This information is determined by examination of the G1 byte in the PLCP frame.')
forePlcpTotalYellowAlarmSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forePlcpTotalYellowAlarmSeconds.setStatus('current')
if mibBuilder.loadTexts: forePlcpTotalYellowAlarmSeconds.setDescription('The number of seconds that a far end yellow alarm condition has persisted. This information is determined by examiniation of the G1 byte of the PLCP frame.')
forePlcpCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 3), )
if mibBuilder.loadTexts: forePlcpCurrentTable.setStatus('current')
if mibBuilder.loadTexts: forePlcpCurrentTable.setDescription('A table of PLCP convergence layer information and parameters.')
forePlcpCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: forePlcpCurrentEntry.setStatus('current')
if mibBuilder.loadTexts: forePlcpCurrentEntry.setDescription('A table entry containing PLCP convergence layer current statistics for each atm interface using PLCP.')
forePlcpCurrentFerrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forePlcpCurrentFerrCount.setStatus('current')
if mibBuilder.loadTexts: forePlcpCurrentFerrCount.setDescription('The number of framing errors detected in current interval. A framing error is determined by errors in the A1 and A2 bytes of the PLCP frame.')
forePlcpCurrentBip8Count = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forePlcpCurrentBip8Count.setStatus('current')
if mibBuilder.loadTexts: forePlcpCurrentBip8Count.setDescription('The number of Bit Interleaved Parity errors detected in the current interval. A BIP error is determined by using the parity carried in the B1 byte of the PLCP frame.')
forePlcpCurrentFebeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forePlcpCurrentFebeCount.setStatus('current')
if mibBuilder.loadTexts: forePlcpCurrentFebeCount.setDescription('The number of Far End BIP Errors detected in the current interval. This information is determined by examination of the G1 byte in the PLCP frame.')
forePlcpCurrentErrSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forePlcpCurrentErrSeconds.setStatus('current')
if mibBuilder.loadTexts: forePlcpCurrentErrSeconds.setDescription('Number of Errored Seconds in current interval')
forePlcpCurrentSevErrSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forePlcpCurrentSevErrSeconds.setStatus('current')
if mibBuilder.loadTexts: forePlcpCurrentSevErrSeconds.setDescription('Number of Severely Errored Seconds in current interval')
forePlcpCurrentUnavailSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forePlcpCurrentUnavailSeconds.setStatus('current')
if mibBuilder.loadTexts: forePlcpCurrentUnavailSeconds.setDescription('Number of Unavailable Seconds in the current interval')
forePlcpIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 4), )
if mibBuilder.loadTexts: forePlcpIntervalTable.setStatus('current')
if mibBuilder.loadTexts: forePlcpIntervalTable.setDescription('Interval table of PLCP convergence layer information and parameters.')
forePlcpIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "Fore-PLCP-MIB", "forePlcpInterval"))
if mibBuilder.loadTexts: forePlcpIntervalEntry.setStatus('current')
if mibBuilder.loadTexts: forePlcpIntervalEntry.setDescription('A table entry containing PLCP convergence layer current statistics for each atm interface using PLCP.')
forePlcpInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forePlcpInterval.setStatus('current')
if mibBuilder.loadTexts: forePlcpInterval.setDescription('Interval number')
forePlcpIntervalFerrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forePlcpIntervalFerrCount.setStatus('current')
if mibBuilder.loadTexts: forePlcpIntervalFerrCount.setDescription('The number of framing errors detected in particular interval. A framing error is determined by errors in the A1 and A2 bytes of the PLCP frame.')
forePlcpIntervalBip8Count = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forePlcpIntervalBip8Count.setStatus('current')
if mibBuilder.loadTexts: forePlcpIntervalBip8Count.setDescription('The number of Bit Interleaved Parity errors detected in the particular interval. A BIP error is determined by using the parity carried in the B1 byte of the PLCP frame.')
forePlcpIntervalFebeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forePlcpIntervalFebeCount.setStatus('current')
if mibBuilder.loadTexts: forePlcpIntervalFebeCount.setDescription('The number of Far End BIP Errors detected in the particular interval. This information is determined by examination of the G1 byte in the PLCP frame.')
forePlcpIntervalErrSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forePlcpIntervalErrSeconds.setStatus('current')
if mibBuilder.loadTexts: forePlcpIntervalErrSeconds.setDescription('Number of Errored Seconds in particular interval')
forePlcpIntervalSevErrSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forePlcpIntervalSevErrSeconds.setStatus('current')
if mibBuilder.loadTexts: forePlcpIntervalSevErrSeconds.setDescription('Number of Severely Errored Seconds in particular interval')
forePlcpIntervalUnavailSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: forePlcpIntervalUnavailSeconds.setStatus('current')
if mibBuilder.loadTexts: forePlcpIntervalUnavailSeconds.setDescription('Number of Unavailable Seconds in the particular interval')
forePlcpYellowDetected = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifName"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: forePlcpYellowDetected.setStatus('current')
if mibBuilder.loadTexts: forePlcpYellowDetected.setDescription('This trap indicates that the specified DS3 port has detected incoming PLCP Yellow Alarm.')
forePlcpYellowCleared = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifName"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: forePlcpYellowCleared.setStatus('current')
if mibBuilder.loadTexts: forePlcpYellowCleared.setDescription('This trap indicates that the specified DS3 port has detected clearance of incoming PLCP Yellow Alarm.')
forePlcpLOFDetected = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifName"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: forePlcpLOFDetected.setStatus('current')
if mibBuilder.loadTexts: forePlcpLOFDetected.setDescription('This trap indicates that the specified DS3 port has detected incoming PLCP LOF Alarm.')
forePlcpLOFCleared = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifName"), ("Fore-TrapLog-MIB", "trapLogIndex"))
if mibBuilder.loadTexts: forePlcpLOFCleared.setStatus('current')
if mibBuilder.loadTexts: forePlcpLOFCleared.setDescription('This trap indicates that the specified DS3 port has detected clearance of incoming PLCP LOF Alarm.')
mibBuilder.exportSymbols("Fore-PLCP-MIB", forePlcpCurrentSevErrSeconds=forePlcpCurrentSevErrSeconds, forePlcpConfigTable=forePlcpConfigTable, forePlcpIntervalTable=forePlcpIntervalTable, forePlcpCurrentFebeCount=forePlcpCurrentFebeCount, forePlcpTotalBip8Count=forePlcpTotalBip8Count, forePlcpCurrentUnavailSeconds=forePlcpCurrentUnavailSeconds, forePlcpIntervalBip8Count=forePlcpIntervalBip8Count, forePlcpMib=forePlcpMib, forePlcpConfigEntry=forePlcpConfigEntry, forePlcpIntervalErrSeconds=forePlcpIntervalErrSeconds, forePlcpLOFDetected=forePlcpLOFDetected, forePlcpTotalYellowAlarmSeconds=forePlcpTotalYellowAlarmSeconds, forePlcpLOFCleared=forePlcpLOFCleared, forePlcpInterval=forePlcpInterval, forePlcpYellowDetected=forePlcpYellowDetected, forePlcpIntervalSevErrSeconds=forePlcpIntervalSevErrSeconds, forePlcpCurrentFerrCount=forePlcpCurrentFerrCount, forePlcpCurrentTable=forePlcpCurrentTable, forePlcpCurrentEntry=forePlcpCurrentEntry, forePlcpCurrentBip8Count=forePlcpCurrentBip8Count, forePlcpIntervalFebeCount=forePlcpIntervalFebeCount, forePlcpTotalEntry=forePlcpTotalEntry, forePlcpIntervalUnavailSeconds=forePlcpIntervalUnavailSeconds, PYSNMP_MODULE_ID=forePlcpMib, forePlcpTotalTable=forePlcpTotalTable, forePlcpTotalFerrCount=forePlcpTotalFerrCount, forePlcpIntervalEntry=forePlcpIntervalEntry, forePlcpConfigFrameFormat=forePlcpConfigFrameFormat, forePlcpTotalLofSeconds=forePlcpTotalLofSeconds, forePlcpTotalFebeCount=forePlcpTotalFebeCount, forePlcpIntervalFerrCount=forePlcpIntervalFerrCount, forePlcpYellowCleared=forePlcpYellowCleared, forePlcpCurrentErrSeconds=forePlcpCurrentErrSeconds)