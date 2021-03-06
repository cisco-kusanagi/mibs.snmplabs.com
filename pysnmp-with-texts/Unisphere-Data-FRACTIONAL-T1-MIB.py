#
# PySNMP MIB module Unisphere-Data-FRACTIONAL-T1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-FRACTIONAL-T1-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:31:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, MibIdentifier, iso, Unsigned32, Bits, IpAddress, TimeTicks, Counter64, Gauge32, Counter32, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "MibIdentifier", "iso", "Unsigned32", "Bits", "IpAddress", "TimeTicks", "Counter64", "Gauge32", "Counter32", "NotificationType", "ObjectIdentity")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdNextIfIndex, UsdTimeSlotMap = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdNextIfIndex", "UsdTimeSlotMap")
usdFt1MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6))
usdFt1MIB.setRevisions(('2000-09-26 17:30', '1999-07-14 00:00', '1998-11-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdFt1MIB.setRevisionsDescriptions(('Make it SMIv2 conformant.', 'Obsoleted usdFt1IfDataPolarity and updated corresponding compliances.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: usdFt1MIB.setLastUpdated('200009261730Z')
if mibBuilder.loadTexts: usdFt1MIB.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdFt1MIB.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford MA 01886 USA Tel: +1 978 589 5800 Email: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdFt1MIB.setDescription('The Fractional T1 MIB for the Unisphere Networks Inc. enterprise.')
usdFt1Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1))
usdFt1NextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 1), UsdNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdFt1NextIfIndex.setStatus('current')
if mibBuilder.loadTexts: usdFt1NextIfIndex.setDescription('Coordinate ifIndex value allocation for entries in usdFt1IfTable. A GET of this object returns the next available ifIndex value to be used to create an entry in the associated interface table; or zero, if no valid ifIndex value is available. This object also returns a value of zero when it is the lexicographic successor of a varbind presented in an SNMP GETNEXT or GETBULK request, for which circumstance it is assumed that ifIndex allocation is unintended. Successive GETs will typically return different values, thus avoiding collisions among cooperating management clients seeking to create table entries simultaneously. ')
usdFt1IfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2), )
if mibBuilder.loadTexts: usdFt1IfTable.setStatus('current')
if mibBuilder.loadTexts: usdFt1IfTable.setDescription('This table contains entries for FT1 interfaces present in the system.')
usdFt1IfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1), ).setIndexNames((0, "Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfIndex"))
if mibBuilder.loadTexts: usdFt1IfEntry.setStatus('current')
if mibBuilder.loadTexts: usdFt1IfEntry.setDescription('Each entry describes the characteristics of an FT1 interface. Creating/deleting entries in this table causes corresponding entries for be created /deleted in ifTable/ifXTable/usdIfTable.')
usdFt1IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: usdFt1IfIndex.setStatus('current')
if mibBuilder.loadTexts: usdFt1IfIndex.setDescription('The ifIndex of the FT1 interface. When creating entries in this table, suitable values for this object are determined by reading usdFt1NextIfIndex.')
usdFt1IfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdFt1IfRowStatus.setStatus('current')
if mibBuilder.loadTexts: usdFt1IfRowStatus.setDescription('Controls creation/deletion of entries in this table according to the RowStatus textual convention, constrained to support the following values only: createAndGo destroy To create an entry in this table, the following entry objects MUST be explicitly configured: usdFt1IfRowStatus usdFt1IfLowerIfIndex usdFt1IfTimeSlotMap In addition, when creating an entry the following conditions must hold: A value for usdFt1IfIndex must have been determined previously, by reading usdFt1NextIfIndex. The DS1 interface identified by usdFt1IfLowerIfIndex must exist. The DS0s specified in usdFt1IfTimeSlotMap must be available (unallocated) on the DS1 interface identified by usdFt1IfLowerIfIndex. A corresponding entry in ifTable/ifXTable/usdIfTable is created/destroyed as a result of creating/destroying an entry in this table. ')
usdFt1IfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdFt1IfLowerIfIndex.setStatus('current')
if mibBuilder.loadTexts: usdFt1IfLowerIfIndex.setDescription('The ifIndex of a DS1 interface over which this FT1 interface is to be layered. A value of zero indicates no layering. An implementation may choose to require that a nonzero value be configured at entry creation.')
usdFt1IfTimeSlotMap = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 4), UsdTimeSlotMap()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdFt1IfTimeSlotMap.setStatus('current')
if mibBuilder.loadTexts: usdFt1IfTimeSlotMap.setDescription('A bitmap representing the DS0s on the underlying DS1 interface that have been allocated to this FT1 interface.')
usdFt1IfTimeSlotRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("nx56kbps", 0), ("nx64kbps", 1))).clone('nx64kbps')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdFt1IfTimeSlotRate.setStatus('current')
if mibBuilder.loadTexts: usdFt1IfTimeSlotRate.setDescription('Data rate per time slot allocated to this FT1 interface.')
usdFt1IfDataPolarity = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normal", 0), ("inverted", 1))).clone('normal')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdFt1IfDataPolarity.setStatus('obsolete')
if mibBuilder.loadTexts: usdFt1IfDataPolarity.setDescription("Polarity of data transmitted on this FT1 interface. Inverted data is used for certain line coding configurations to ensure sufficient one's density for timing recovery by the remote end.")
usdFt1IfLoopbackConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("noLoop", 0), ("loop", 1))).clone('noLoop')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdFt1IfLoopbackConfig.setStatus('current')
if mibBuilder.loadTexts: usdFt1IfLoopbackConfig.setDescription('Selects loopback configuration. loop(1) causes received data to be looped back out the transmitter.')
usdFt1Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4))
usdFt1Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 1))
usdFt1Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 2))
usdFt1Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 1, 1)).setObjects(("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFt1Compliance = usdFt1Compliance.setStatus('obsolete')
if mibBuilder.loadTexts: usdFt1Compliance.setDescription('The compliance statement for entities that implement the Unisphere FT1 MIB.')
usdFt1Compliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 1, 2)).setObjects(("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1Group2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFt1Compliance2 = usdFt1Compliance2.setStatus('current')
if mibBuilder.loadTexts: usdFt1Compliance2.setDescription('The compliance statement for entities that implement the Unisphere FT1 MIB.')
usdFt1Group = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 2, 1)).setObjects(("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1NextIfIndex"), ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfRowStatus"), ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfLowerIfIndex"), ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfTimeSlotMap"), ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfTimeSlotRate"), ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfDataPolarity"), ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfLoopbackConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFt1Group = usdFt1Group.setStatus('obsolete')
if mibBuilder.loadTexts: usdFt1Group.setDescription('A collection of objects providing management of FT1 interfaces in a Unisphere product.')
usdFt1Group2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 2, 2)).setObjects(("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1NextIfIndex"), ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfRowStatus"), ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfLowerIfIndex"), ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfTimeSlotMap"), ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfTimeSlotRate"), ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfLoopbackConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFt1Group2 = usdFt1Group2.setStatus('current')
if mibBuilder.loadTexts: usdFt1Group2.setDescription('A collection of objects providing management of FT1 interfaces in a Unisphere product.')
mibBuilder.exportSymbols("Unisphere-Data-FRACTIONAL-T1-MIB", PYSNMP_MODULE_ID=usdFt1MIB, usdFt1IfTimeSlotRate=usdFt1IfTimeSlotRate, usdFt1IfLoopbackConfig=usdFt1IfLoopbackConfig, usdFt1Group=usdFt1Group, usdFt1NextIfIndex=usdFt1NextIfIndex, usdFt1IfIndex=usdFt1IfIndex, usdFt1IfTimeSlotMap=usdFt1IfTimeSlotMap, usdFt1IfTable=usdFt1IfTable, usdFt1Conformance=usdFt1Conformance, usdFt1Group2=usdFt1Group2, usdFt1IfLowerIfIndex=usdFt1IfLowerIfIndex, usdFt1Compliances=usdFt1Compliances, usdFt1MIB=usdFt1MIB, usdFt1Compliance2=usdFt1Compliance2, usdFt1IfDataPolarity=usdFt1IfDataPolarity, usdFt1IfRowStatus=usdFt1IfRowStatus, usdFt1Objects=usdFt1Objects, usdFt1Groups=usdFt1Groups, usdFt1Compliance=usdFt1Compliance, usdFt1IfEntry=usdFt1IfEntry)
