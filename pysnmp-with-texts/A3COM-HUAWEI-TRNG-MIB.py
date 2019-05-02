#
# PySNMP MIB module A3COM-HUAWEI-TRNG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-TRNG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:07:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
huaweiDatacomm, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "huaweiDatacomm")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, MibIdentifier, iso, ModuleIdentity, TimeTicks, Bits, Counter32, ObjectIdentity, IpAddress, Counter64, NotificationType, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "iso", "ModuleIdentity", "TimeTicks", "Bits", "Counter32", "ObjectIdentity", "IpAddress", "Counter64", "NotificationType", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, DateAndTime, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DateAndTime", "RowStatus", "TextualConvention", "DisplayString")
hwTRNG = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13))
hwTRNG.setRevisions(('2003-04-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwTRNG.setRevisionsDescriptions(('200304110000Z, --The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hwTRNG.setLastUpdated('200304110000Z')
if mibBuilder.loadTexts: hwTRNG.setOrganization('Huawei Technologies Co., Ltd.')
if mibBuilder.loadTexts: hwTRNG.setContactInfo('R&D BeiJing, Huawei Technologies co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China Zip:100085 Http://www.huawei.com E-mail:support@huawei.com')
if mibBuilder.loadTexts: hwTRNG.setDescription('The A3COM-HUAWEI-TRNG-MIB contains objects to Configure the system absolute and periodic time-range.')
hwTRNGMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 1))
hwTrngCreateTimerangeTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 1, 1), )
if mibBuilder.loadTexts: hwTrngCreateTimerangeTable.setStatus('current')
if mibBuilder.loadTexts: hwTrngCreateTimerangeTable.setDescription('Creat TimeRange.')
hwTrngCreateTimerangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-TRNG-MIB", "hwTrngIndex"))
if mibBuilder.loadTexts: hwTrngCreateTimerangeEntry.setStatus('current')
if mibBuilder.loadTexts: hwTrngCreateTimerangeEntry.setDescription('Define the entry of hwTrngCreateTimerangeTable')
hwTrngIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256)))
if mibBuilder.loadTexts: hwTrngIndex.setStatus('current')
if mibBuilder.loadTexts: hwTrngIndex.setDescription("TimeRange's index")
hwTrngName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTrngName.setStatus('current')
if mibBuilder.loadTexts: hwTrngName.setDescription("TimeRange's name")
hwTrngValidFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 1, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTrngValidFlag.setStatus('current')
if mibBuilder.loadTexts: hwTrngValidFlag.setDescription('Valid or Invalid flag')
hwTrngCreateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTrngCreateRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwTrngCreateRowStatus.setDescription('The status of this conceptual row.Now only realize CreateAndGo and Destroy and Active.')
hwTrngAbsoluteTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 1, 2), )
if mibBuilder.loadTexts: hwTrngAbsoluteTable.setStatus('current')
if mibBuilder.loadTexts: hwTrngAbsoluteTable.setDescription('Creat absoluteness time item of the TimeRange')
hwTrngAbsoluteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 1, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-TRNG-MIB", "hwTrngAbsoluteNameIndex"), (0, "A3COM-HUAWEI-TRNG-MIB", "hwTrngAbsoluteSubIndex"))
if mibBuilder.loadTexts: hwTrngAbsoluteEntry.setStatus('current')
if mibBuilder.loadTexts: hwTrngAbsoluteEntry.setDescription('Define the entry of hwTrngAbsoluteTable')
hwTrngAbsoluteNameIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256)))
if mibBuilder.loadTexts: hwTrngAbsoluteNameIndex.setStatus('current')
if mibBuilder.loadTexts: hwTrngAbsoluteNameIndex.setDescription("TimeRange's index")
hwTrngAbsoluteSubIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12)))
if mibBuilder.loadTexts: hwTrngAbsoluteSubIndex.setStatus('current')
if mibBuilder.loadTexts: hwTrngAbsoluteSubIndex.setDescription("SubItem's index")
hwTimerangeAbsoluteStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 1, 2, 1, 3), DateAndTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTimerangeAbsoluteStartTime.setStatus('current')
if mibBuilder.loadTexts: hwTimerangeAbsoluteStartTime.setDescription("Start point of the timerange.The format defined like 'YYYY-MM-DD,hh:mm:0.0'.")
hwTimerangeAbsoluteEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 1, 2, 1, 4), DateAndTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTimerangeAbsoluteEndTime.setStatus('current')
if mibBuilder.loadTexts: hwTimerangeAbsoluteEndTime.setDescription("End point of the timerange.The format defined like 'YYYY-MM-DD,hh:mm:0.0'.")
hwTimerangeAbsolueRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTimerangeAbsolueRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwTimerangeAbsolueRowStatus.setDescription('The status of this conceptual row. Now only realize CreateAndGo and Destroy and Active.')
hwTrngPeriodicTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 1, 3), )
if mibBuilder.loadTexts: hwTrngPeriodicTable.setStatus('current')
if mibBuilder.loadTexts: hwTrngPeriodicTable.setDescription('Creat periodic time item of the TimeRange')
hwTrngPeriodicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 1, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-TRNG-MIB", "hwTrngPeriodicNameIndex"), (0, "A3COM-HUAWEI-TRNG-MIB", "hwTrngPeriodicSubIndex"))
if mibBuilder.loadTexts: hwTrngPeriodicEntry.setStatus('current')
if mibBuilder.loadTexts: hwTrngPeriodicEntry.setDescription('Define the index of hwTrngPeriodicTable')
hwTrngPeriodicNameIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256)))
if mibBuilder.loadTexts: hwTrngPeriodicNameIndex.setStatus('current')
if mibBuilder.loadTexts: hwTrngPeriodicNameIndex.setDescription("TimeRange's index")
hwTrngPeriodicSubIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: hwTrngPeriodicSubIndex.setStatus('current')
if mibBuilder.loadTexts: hwTrngPeriodicSubIndex.setDescription("SubItem's index")
hwTrngPeriodicDayOfWeek = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 1, 3, 1, 3), Bits().clone(namedValues=NamedValues(("sunday", 0), ("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTrngPeriodicDayOfWeek.setStatus('current')
if mibBuilder.loadTexts: hwTrngPeriodicDayOfWeek.setDescription('The day of week. This is a bit-map of possible conditions. The various bit positions are: |0 |sunday | |1 |monday | |2 |tuesday | |3 |wednesday | |4 |thursday | |5 |friday | |6 |saturday | ')
hwTimerangePeriodicStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 1, 3, 1, 4), DateAndTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTimerangePeriodicStartTime.setStatus('current')
if mibBuilder.loadTexts: hwTimerangePeriodicStartTime.setDescription("Start point of this timerange,The format defined like 'hh:mm:0,0'.")
hwTimerangePeriodicEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 1, 3, 1, 5), DateAndTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTimerangePeriodicEndTime.setStatus('current')
if mibBuilder.loadTexts: hwTimerangePeriodicEndTime.setDescription("End point of this timerange. The format definedlike 'hh:mm:0,0'.")
hwTimerangePeriodicRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTimerangePeriodicRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwTimerangePeriodicRowStatus.setDescription('The status of this conceptual row, Now only realize CreateAndGo and Destroy and Active.')
hwTRNGMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 3))
hwTRNGMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 3, 1))
hwTRNGMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 3, 1, 1)).setObjects(("A3COM-HUAWEI-TRNG-MIB", "hwTRNGGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTRNGMibCompliance = hwTRNGMibCompliance.setStatus('current')
if mibBuilder.loadTexts: hwTRNGMibCompliance.setDescription('The compliance statement for entities which implement the Huawei Time-range MIB.')
hwTRNGMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 3, 2))
hwTRNGGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 13, 3, 2, 1)).setObjects(("A3COM-HUAWEI-TRNG-MIB", "hwTrngName"), ("A3COM-HUAWEI-TRNG-MIB", "hwTrngValidFlag"), ("A3COM-HUAWEI-TRNG-MIB", "hwTrngCreateRowStatus"), ("A3COM-HUAWEI-TRNG-MIB", "hwTimerangeAbsoluteStartTime"), ("A3COM-HUAWEI-TRNG-MIB", "hwTimerangeAbsoluteEndTime"), ("A3COM-HUAWEI-TRNG-MIB", "hwTimerangeAbsolueRowStatus"), ("A3COM-HUAWEI-TRNG-MIB", "hwTrngPeriodicDayOfWeek"), ("A3COM-HUAWEI-TRNG-MIB", "hwTimerangePeriodicStartTime"), ("A3COM-HUAWEI-TRNG-MIB", "hwTimerangePeriodicEndTime"), ("A3COM-HUAWEI-TRNG-MIB", "hwTimerangePeriodicRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTRNGGroup = hwTRNGGroup.setStatus('current')
if mibBuilder.loadTexts: hwTRNGGroup.setDescription('A collection of objects providing mandatory time-range information.')
mibBuilder.exportSymbols("A3COM-HUAWEI-TRNG-MIB", hwTRNGMibObjects=hwTRNGMibObjects, hwTimerangeAbsoluteStartTime=hwTimerangeAbsoluteStartTime, hwTimerangePeriodicRowStatus=hwTimerangePeriodicRowStatus, hwTimerangeAbsoluteEndTime=hwTimerangeAbsoluteEndTime, hwTRNGMibCompliances=hwTRNGMibCompliances, hwTRNGMibConformance=hwTRNGMibConformance, hwTrngPeriodicTable=hwTrngPeriodicTable, hwTrngValidFlag=hwTrngValidFlag, hwTRNG=hwTRNG, hwTrngIndex=hwTrngIndex, hwTrngAbsoluteSubIndex=hwTrngAbsoluteSubIndex, hwTRNGMibCompliance=hwTRNGMibCompliance, hwTrngCreateRowStatus=hwTrngCreateRowStatus, hwTrngPeriodicEntry=hwTrngPeriodicEntry, hwTrngAbsoluteEntry=hwTrngAbsoluteEntry, hwTrngPeriodicDayOfWeek=hwTrngPeriodicDayOfWeek, hwTimerangeAbsolueRowStatus=hwTimerangeAbsolueRowStatus, PYSNMP_MODULE_ID=hwTRNG, hwTimerangePeriodicStartTime=hwTimerangePeriodicStartTime, hwTrngAbsoluteTable=hwTrngAbsoluteTable, hwTrngPeriodicSubIndex=hwTrngPeriodicSubIndex, hwTrngAbsoluteNameIndex=hwTrngAbsoluteNameIndex, hwTRNGGroup=hwTRNGGroup, hwTrngCreateTimerangeEntry=hwTrngCreateTimerangeEntry, hwTrngPeriodicNameIndex=hwTrngPeriodicNameIndex, hwTRNGMibGroups=hwTRNGMibGroups, hwTimerangePeriodicEndTime=hwTimerangePeriodicEndTime, hwTrngCreateTimerangeTable=hwTrngCreateTimerangeTable, hwTrngName=hwTrngName)
