#
# PySNMP MIB module CISCO-P2P-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-P2P-IF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:09:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, ObjectIdentity, Unsigned32, Counter32, Integer32, Counter64, ModuleIdentity, IpAddress, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "Unsigned32", "Counter32", "Integer32", "Counter64", "ModuleIdentity", "IpAddress", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoP2PIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 668))
ciscoP2PIfMIB.setRevisions(('2008-08-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoP2PIfMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoP2PIfMIB.setLastUpdated('200808120000Z')
if mibBuilder.loadTexts: ciscoP2PIfMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoP2PIfMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: q-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoP2PIfMIB.setDescription('The Point to Point Interface MIB module. This MIB manages the generic objects for Serial link or SONET/SDH like point to point network interfaces with the encapsulations of PPP (Point to Point Protocol), HDLC (High Level Data Link Control) or cHDLC (CIsco extension to High Level Data Link Control) framing. Acronyms and terms: FCS - Frame Check Sequence. The frame check sequence is used to ensure that the data received is actually the data sent. CRC - Cyclic Redundancy Check. The transmitting system processes the frame check sequence portion of the frame through an algorithm called a CRC (Cyclic Redundancy Check). One of the usages of CRC is in the following PPP/HLDC over SONET/SDH example. +----+ | PPP| FCS Bit SONET/SDH |HDLC|=> Generation => Stuffing => Scrambling => Framing +----+ CRC 16,32')
ciscoP2PIfMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 0))
ciscoP2PIfMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 1))
cp2pIfGeneralObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1))
class Cp2pIfCrcMode(TextualConvention, Integer32):
    reference = 'RFC-2615, PPP over SONET/SDH: Section 5. Configuration Details.'
    description = 'Specifies the CRC mode of Cyclic Redundancy Check. crc16 - 16-bit CRC. crc32 - 32-bit CRC.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("crc16", 1), ("crc32", 2))

class Cp2pIfScramblingMode(TextualConvention, Integer32):
    reference = 'RFC-2615, PPP over SONET/SDH: Section 4. X**43 + 1 Scrambler Description.'
    description = 'An enumerated value of the Scrambling encryption mode of an interface. on - scrambling encryption enabled. off - scrambling encryption disabled.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("off", 2))

cp2pIfCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1), )
if mibBuilder.loadTexts: cp2pIfCfgTable.setStatus('current')
if mibBuilder.loadTexts: cp2pIfCfgTable.setDescription('The Point to Point generic Configuration Table. It contains the standard configuration information of the Point to Point interface.')
cp2pIfCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cp2pIfCfgEntry.setStatus('current')
if mibBuilder.loadTexts: cp2pIfCfgEntry.setDescription('An entry in the configuration table for each Point to Point interface. The entry is created when the Point to Point related interface is created in ifTable. The possible ifType of point to point interface are listed as follows: [1] ppp(23) [2] hdlc(118) [3] propPointToPointSerial(22)')
cp2pIfCfgCrcMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1, 1, 1), Cp2pIfCrcMode().clone('crc32')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cp2pIfCfgCrcMode.setStatus('current')
if mibBuilder.loadTexts: cp2pIfCfgCrcMode.setDescription('Specifies the CRC mode for the FCS generation of a packet sending via the Point to point interface.')
cp2pIfCfgScramblingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1, 1, 2), Cp2pIfScramblingMode().clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cp2pIfCfgScramblingMode.setStatus('current')
if mibBuilder.loadTexts: cp2pIfCfgScramblingMode.setDescription('Specifies the scrambling encryption mode of the point to point interface.')
cp2pIfCfgTransmitDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 18000))).setUnits('microseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cp2pIfCfgTransmitDelay.setStatus('current')
if mibBuilder.loadTexts: cp2pIfCfgTransmitDelay.setDescription("Specified the minimum delay after sending a packet via the point to point interface. The value of '0' indicates the transmit delay of packet is disabled.")
cp2pIfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 2), )
if mibBuilder.loadTexts: cp2pIfStatsTable.setStatus('current')
if mibBuilder.loadTexts: cp2pIfStatsTable.setDescription('The Point to Point Interface Statistics Table. It contains statistics information of a Point to Point interface including the error statistics.')
cp2pIfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 2, 1), )
cp2pIfCfgEntry.registerAugmentions(("CISCO-P2P-IF-MIB", "cp2pIfStatsEntry"))
cp2pIfStatsEntry.setIndexNames(*cp2pIfCfgEntry.getIndexNames())
if mibBuilder.loadTexts: cp2pIfStatsEntry.setStatus('current')
if mibBuilder.loadTexts: cp2pIfStatsEntry.setDescription('An entry in the statistics table for each Point to Point interface.')
cp2pIfStatsInCrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cp2pIfStatsInCrcErrors.setStatus('current')
if mibBuilder.loadTexts: cp2pIfStatsInCrcErrors.setDescription('Accumulated number of CRC errors that are detected on the received packets via the Point to Point interface since system startup.')
ciscoP2PIfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 3))
ciscoP2PIfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 3, 1))
ciscoP2PIfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 3, 2))
ciscoP2PIfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 668, 3, 1, 1)).setObjects(("CISCO-P2P-IF-MIB", "ciscoP2PIfMIBGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2PIfMIBCompliance = ciscoP2PIfMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoP2PIfMIBCompliance.setDescription('The compliance statement for entities which implement the Cisco Point to Point interface MIB')
ciscoP2PIfMIBGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 668, 3, 2, 1)).setObjects(("CISCO-P2P-IF-MIB", "cp2pIfCfgCrcMode"), ("CISCO-P2P-IF-MIB", "cp2pIfCfgScramblingMode"), ("CISCO-P2P-IF-MIB", "cp2pIfCfgTransmitDelay"), ("CISCO-P2P-IF-MIB", "cp2pIfStatsInCrcErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2PIfMIBGeneralGroup = ciscoP2PIfMIBGeneralGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoP2PIfMIBGeneralGroup.setDescription('The collection of objects providing general information about the Cisco Point to Point interfaces.')
mibBuilder.exportSymbols("CISCO-P2P-IF-MIB", ciscoP2PIfMIBNotifs=ciscoP2PIfMIBNotifs, ciscoP2PIfMIBGroups=ciscoP2PIfMIBGroups, ciscoP2PIfMIBGeneralGroup=ciscoP2PIfMIBGeneralGroup, cp2pIfCfgEntry=cp2pIfCfgEntry, PYSNMP_MODULE_ID=ciscoP2PIfMIB, cp2pIfGeneralObjects=cp2pIfGeneralObjects, ciscoP2PIfMIBObjects=ciscoP2PIfMIBObjects, cp2pIfStatsEntry=cp2pIfStatsEntry, cp2pIfStatsInCrcErrors=cp2pIfStatsInCrcErrors, ciscoP2PIfMIBCompliance=ciscoP2PIfMIBCompliance, cp2pIfCfgTable=cp2pIfCfgTable, cp2pIfCfgScramblingMode=cp2pIfCfgScramblingMode, ciscoP2PIfMIB=ciscoP2PIfMIB, ciscoP2PIfMIBConformance=ciscoP2PIfMIBConformance, cp2pIfCfgCrcMode=cp2pIfCfgCrcMode, Cp2pIfCrcMode=Cp2pIfCrcMode, cp2pIfCfgTransmitDelay=cp2pIfCfgTransmitDelay, Cp2pIfScramblingMode=Cp2pIfScramblingMode, ciscoP2PIfMIBCompliances=ciscoP2PIfMIBCompliances, cp2pIfStatsTable=cp2pIfStatsTable)
