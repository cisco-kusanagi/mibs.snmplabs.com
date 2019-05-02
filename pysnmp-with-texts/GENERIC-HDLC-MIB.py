#
# PySNMP MIB module GENERIC-HDLC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GENERIC-HDLC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:19:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
nnbundleId, = mibBuilder.importSymbols("BUNDLE-MIB", "nnbundleId")
ntEnterpriseDataTasmanMgmt, = mibBuilder.importSymbols("NT-ENTERPRISE-DATA-MIB", "ntEnterpriseDataTasmanMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Gauge32, IpAddress, MibIdentifier, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Unsigned32, iso, TimeTicks, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "IpAddress", "MibIdentifier", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Unsigned32", "iso", "TimeTicks", "Integer32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nngenHdlcMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15))
if mibBuilder.loadTexts: nngenHdlcMib.setLastUpdated('9907010000Z')
if mibBuilder.loadTexts: nngenHdlcMib.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: nngenHdlcMib.setContactInfo(' Nortel Networks 8200 Dixie Road Brampton, Ontario L6T 5P6 Canada 1-800-4Nortel www.nortelnetworks.com ')
if mibBuilder.loadTexts: nngenHdlcMib.setDescription('The MIB defines objects for configuring generic HDLC bundles and thier monitoring')
nngenHdlcTable = MibTable((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 1), )
if mibBuilder.loadTexts: nngenHdlcTable.setStatus('current')
if mibBuilder.loadTexts: nngenHdlcTable.setDescription('All the parameters pertinent to HDLC encapsulation on a bundle are defined in this table.')
nngenHdlcTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 1, 1), ).setIndexNames((0, "BUNDLE-MIB", "nnbundleId"))
if mibBuilder.loadTexts: nngenHdlcTableEntry.setStatus('current')
if mibBuilder.loadTexts: nngenHdlcTableEntry.setDescription('An entry in the GenHdlc Table')
nngenHdlcKeepAlive = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 120)).clone(10)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: nngenHdlcKeepAlive.setStatus('current')
if mibBuilder.loadTexts: nngenHdlcKeepAlive.setDescription("The link's keep-alive interval. System will send messages once every chosen interval to check bundle's status.")
nngenHdlcMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 1, 1, 2), Integer32().clone(1500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nngenHdlcMtu.setStatus('current')
if mibBuilder.loadTexts: nngenHdlcMtu.setDescription('Maximum transmission unit ie. the maximum packet size to be sent.')
nngenHdlcStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2), )
if mibBuilder.loadTexts: nngenHdlcStatsTable.setStatus('current')
if mibBuilder.loadTexts: nngenHdlcStatsTable.setDescription('All the statistics parameters pertinent to HDLC encapsulation on a bundle are defined in this table.')
nngenHdlcStatsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1), ).setIndexNames((0, "BUNDLE-MIB", "nnbundleId"))
if mibBuilder.loadTexts: nngenHdlcStatsTableEntry.setStatus('current')
if mibBuilder.loadTexts: nngenHdlcStatsTableEntry.setDescription('An entry in the genHdlcStats Table')
nngenHdlcStatsBytesRxLastBootClear = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsBytesRxLastBootClear.setStatus('current')
if mibBuilder.loadTexts: nngenHdlcStatsBytesRxLastBootClear.setDescription('')
nngenHdlcStatsBytesTxLastBootClear = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsBytesTxLastBootClear.setStatus('current')
if mibBuilder.loadTexts: nngenHdlcStatsBytesTxLastBootClear.setDescription('')
nngenHdlcStatsPktsRxLastBootClear = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsPktsRxLastBootClear.setStatus('current')
if mibBuilder.loadTexts: nngenHdlcStatsPktsRxLastBootClear.setDescription('')
nngenHdlcStatsPktsTxLastBootClear = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsPktsTxLastBootClear.setStatus('current')
if mibBuilder.loadTexts: nngenHdlcStatsPktsTxLastBootClear.setDescription('')
nngenHdlcStatsErrPktsRxLastBootClear = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsErrPktsRxLastBootClear.setStatus('current')
if mibBuilder.loadTexts: nngenHdlcStatsErrPktsRxLastBootClear.setDescription('')
nngenHdlcStatsUpDownStatesLastBootClear = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsUpDownStatesLastBootClear.setStatus('current')
if mibBuilder.loadTexts: nngenHdlcStatsUpDownStatesLastBootClear.setDescription('')
nngenHdlcStatsBytesRxLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsBytesRxLastFiveMins.setStatus('current')
if mibBuilder.loadTexts: nngenHdlcStatsBytesRxLastFiveMins.setDescription('')
nngenHdlcStatsBytesTxLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsBytesTxLastFiveMins.setStatus('current')
if mibBuilder.loadTexts: nngenHdlcStatsBytesTxLastFiveMins.setDescription('')
nngenHdlcStatsPktsRxLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsPktsRxLastFiveMins.setStatus('current')
if mibBuilder.loadTexts: nngenHdlcStatsPktsRxLastFiveMins.setDescription('')
nngenHdlcStatsPktsTxLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsPktsTxLastFiveMins.setStatus('current')
if mibBuilder.loadTexts: nngenHdlcStatsPktsTxLastFiveMins.setDescription('')
nngenHdlcStatsErrPktsRxLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsErrPktsRxLastFiveMins.setStatus('current')
if mibBuilder.loadTexts: nngenHdlcStatsErrPktsRxLastFiveMins.setDescription('')
nngenHdlcStatsUpDownStatesLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 15, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nngenHdlcStatsUpDownStatesLastFiveMins.setStatus('current')
if mibBuilder.loadTexts: nngenHdlcStatsUpDownStatesLastFiveMins.setDescription('')
mibBuilder.exportSymbols("GENERIC-HDLC-MIB", nngenHdlcMtu=nngenHdlcMtu, nngenHdlcStatsUpDownStatesLastFiveMins=nngenHdlcStatsUpDownStatesLastFiveMins, nngenHdlcStatsPktsRxLastFiveMins=nngenHdlcStatsPktsRxLastFiveMins, nngenHdlcStatsTable=nngenHdlcStatsTable, nngenHdlcStatsErrPktsRxLastFiveMins=nngenHdlcStatsErrPktsRxLastFiveMins, nngenHdlcTable=nngenHdlcTable, PYSNMP_MODULE_ID=nngenHdlcMib, nngenHdlcStatsBytesTxLastBootClear=nngenHdlcStatsBytesTxLastBootClear, nngenHdlcStatsBytesTxLastFiveMins=nngenHdlcStatsBytesTxLastFiveMins, nngenHdlcStatsPktsTxLastFiveMins=nngenHdlcStatsPktsTxLastFiveMins, nngenHdlcKeepAlive=nngenHdlcKeepAlive, nngenHdlcStatsBytesRxLastBootClear=nngenHdlcStatsBytesRxLastBootClear, nngenHdlcStatsErrPktsRxLastBootClear=nngenHdlcStatsErrPktsRxLastBootClear, nngenHdlcStatsBytesRxLastFiveMins=nngenHdlcStatsBytesRxLastFiveMins, nngenHdlcStatsTableEntry=nngenHdlcStatsTableEntry, nngenHdlcStatsPktsRxLastBootClear=nngenHdlcStatsPktsRxLastBootClear, nngenHdlcStatsUpDownStatesLastBootClear=nngenHdlcStatsUpDownStatesLastBootClear, nngenHdlcMib=nngenHdlcMib, nngenHdlcTableEntry=nngenHdlcTableEntry, nngenHdlcStatsPktsTxLastBootClear=nngenHdlcStatsPktsTxLastBootClear)
