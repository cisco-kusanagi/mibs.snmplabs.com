#
# PySNMP MIB module Unisphere-Data-V35-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-V35-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:33:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, Bits, Counter64, Gauge32, IpAddress, MibIdentifier, TimeTicks, ObjectIdentity, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Counter64", "Gauge32", "IpAddress", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
usdV35MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 59))
usdV35MIB.setRevisions(('2002-02-08 16:25',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdV35MIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: usdV35MIB.setLastUpdated('200202081625Z')
if mibBuilder.loadTexts: usdV35MIB.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdV35MIB.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 Email: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdV35MIB.setDescription('The X.21/V.35 Server MIB for the Unisphere Networks enterprise.')
usdV35Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1))
usdV35IfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2), )
if mibBuilder.loadTexts: usdV35IfTable.setStatus('current')
if mibBuilder.loadTexts: usdV35IfTable.setDescription('This table contains entries for X.21/V.35 interfaces present in the system. This table provides an extension to the Unisphere-Data-HDLC-MIB.usdHdlcIfTable for HDLC interfaces that support X.21/V.35 signalling.')
usdV35IfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1), ).setIndexNames((0, "Unisphere-Data-V35-MIB", "usdV35IfIndex"))
if mibBuilder.loadTexts: usdV35IfEntry.setStatus('current')
if mibBuilder.loadTexts: usdV35IfEntry.setDescription('Each entry describes the characteristics of an X.21/V.35 interface.')
usdV35IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: usdV35IfIndex.setStatus('current')
if mibBuilder.loadTexts: usdV35IfIndex.setDescription('The ifIndex of the X.21/V.35 interface. It has the same value as the usdHdlcIfIndex for the common interface.')
usdV35IfType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("x21", 0), ("v35", 1), ("interfaceTypeNoCable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdV35IfType.setStatus('current')
if mibBuilder.loadTexts: usdV35IfType.setDescription('Read only parameter of interface type X.21/V.35.')
usdV35IfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("dte", 0), ("dce", 1), ("interfaceModeNoCable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdV35IfMode.setStatus('current')
if mibBuilder.loadTexts: usdV35IfMode.setDescription('Read only parameter of interface mode of interface X.21/V.35 Data Terminating Equipment(DTE)/Data Communication Equipment(DCE).')
usdV35IfClockRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 4), Unsigned32().clone(2048000)).setUnits('hertz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdV35IfClockRate.setStatus('current')
if mibBuilder.loadTexts: usdV35IfClockRate.setDescription('The clock rate setting in hertz for this X.21/V.35 interface. Only the following values are valid: 1200, 2400, 4800, 9600, 19200, 38400, 56000, 64000, 128000, 1024000, 1536000, 2048000, 3072000, 4096000, 4915200, 6144000, and 8192000. If a value other than one of the predefined values is set, then the closest matching value is used. The clock rate parameter is only meaningful when the interface is in DCE mode. When the interface is in DTE mode, the value is simply ignored.')
usdV35IfNrzEncoding = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normal", 0), ("inverted", 1))).clone('normal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdV35IfNrzEncoding.setStatus('current')
if mibBuilder.loadTexts: usdV35IfNrzEncoding.setDescription('The non-return-to-zero (NRZ) encoding for X.21/V.35 interface. Inverted encoding is provided with NRZI-encoding command, which is non-return-to-zero inverted (NRZI) encoding.')
usdV35IfTxClock = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normal", 0), ("inverted", 1))).clone('normal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdV35IfTxClock.setStatus('current')
if mibBuilder.loadTexts: usdV35IfTxClock.setDescription('There is an option of inverting the transmit clock signal for X.21/V.35 interface. Inverting the tranmit clock is used to compensate for skews between the clock and data when transmitting across long cables at fast data rates.')
usdV35IfIgnoreDcd = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("ignoredNone", 0), ("dcdIgnored", 1), ("linkStateIgnored", 2))).clone('ignoredNone')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdV35IfIgnoreDcd.setStatus('current')
if mibBuilder.loadTexts: usdV35IfIgnoreDcd.setDescription('When in X.21/V.35 DTE mode we have the capability of ignoring the DCD signal in determining whether or not an interface is up.')
usdV35IfLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("loopback", 1))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdV35IfLoopback.setStatus('current')
if mibBuilder.loadTexts: usdV35IfLoopback.setDescription('Loopback interface is configured (or not) for X.21/V.35 interface')
usdV35Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 4))
usdV35Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 4, 1))
usdV35Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 4, 2))
usdV35Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 4, 1, 1)).setObjects(("Unisphere-Data-V35-MIB", "usdV35Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdV35Compliance = usdV35Compliance.setStatus('current')
if mibBuilder.loadTexts: usdV35Compliance.setDescription('The compliance statement for entities that implement the Unisphere X.21/V.35 MIB.')
usdV35Group = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 4, 2, 1)).setObjects(("Unisphere-Data-V35-MIB", "usdV35IfType"), ("Unisphere-Data-V35-MIB", "usdV35IfMode"), ("Unisphere-Data-V35-MIB", "usdV35IfClockRate"), ("Unisphere-Data-V35-MIB", "usdV35IfNrzEncoding"), ("Unisphere-Data-V35-MIB", "usdV35IfTxClock"), ("Unisphere-Data-V35-MIB", "usdV35IfIgnoreDcd"), ("Unisphere-Data-V35-MIB", "usdV35IfLoopback"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdV35Group = usdV35Group.setStatus('current')
if mibBuilder.loadTexts: usdV35Group.setDescription('A collection of objects providing management of X.21/V.35 interfaces in a Unisphere product.')
mibBuilder.exportSymbols("Unisphere-Data-V35-MIB", usdV35Objects=usdV35Objects, usdV35Group=usdV35Group, usdV35IfLoopback=usdV35IfLoopback, PYSNMP_MODULE_ID=usdV35MIB, usdV35Compliances=usdV35Compliances, usdV35Groups=usdV35Groups, usdV35IfType=usdV35IfType, usdV35IfClockRate=usdV35IfClockRate, usdV35IfMode=usdV35IfMode, usdV35IfIgnoreDcd=usdV35IfIgnoreDcd, usdV35IfIndex=usdV35IfIndex, usdV35Compliance=usdV35Compliance, usdV35IfTable=usdV35IfTable, usdV35IfNrzEncoding=usdV35IfNrzEncoding, usdV35IfTxClock=usdV35IfTxClock, usdV35Conformance=usdV35Conformance, usdV35IfEntry=usdV35IfEntry, usdV35MIB=usdV35MIB)
