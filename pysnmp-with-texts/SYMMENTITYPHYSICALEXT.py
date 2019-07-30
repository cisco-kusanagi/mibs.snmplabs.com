#
# PySNMP MIB module SYMMENTITYPHYSICALEXT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMENTITYPHYSICALEXT
# Produced by pysmi-0.3.4 at Tue Jul 30 11:35:00 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
entPhysicalIndex, entPhysicalEntry = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "entPhysicalEntry")
ifIndex, ifNumber = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifNumber")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, Integer32, Gauge32, ModuleIdentity, iso, ObjectIdentity, MibIdentifier, TimeTicks, Counter32, IpAddress, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Gauge32", "ModuleIdentity", "iso", "ObjectIdentity", "MibIdentifier", "TimeTicks", "Counter32", "IpAddress", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
symmEntPhysicalExtension, = mibBuilder.importSymbols("SYMM-COMMON-SMI", "symmEntPhysicalExtension")
symmEntityPhysicalExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1))
symmEntityPhysicalExt.setRevisions(('2016-06-15 10:39',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: symmEntityPhysicalExt.setRevisionsDescriptions(('Symmetricom common entity extension MIB',))
if mibBuilder.loadTexts: symmEntityPhysicalExt.setLastUpdated('201606151039Z')
if mibBuilder.loadTexts: symmEntityPhysicalExt.setOrganization('Symmetricom')
if mibBuilder.loadTexts: symmEntityPhysicalExt.setContactInfo('Symmetricom Technical Support 1-888-367-7966 toll free USA 1-408-428-7907 worldwide Support@symmetricom.com')
if mibBuilder.loadTexts: symmEntityPhysicalExt.setDescription('Symmetricom common entity extension MIB')
class DateAndTime(TextualConvention, OctetString):
    description = "A date-time specification. field octets contents range ----- ------ -------- ----- 1 1-2 year* 0..65536 2 3 month 1..12 3 4 day 1..31 4 5 hour 0..23 5 6 minutes 0..59 6 7 seconds 0..60 (use 60 for leap-second) 7 8 deci-seconds 0..9 8 9 direction from UTC '+' / '-' 9 10 hours from UTC* 0..13 10 11 minutes from UTC 0..59 * Notes: - the value of year is in network-byte order - daylight saving time in New Zealand is +13 For example, Tuesday May 26, 1992 at 1:30:15 PM EDT would be displayed as: 1992-5-26,13:30:15.0,-4:0 Note that if only local time is known, then timezone information (fields 8-10) is not present."
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d:1d.1d,1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
class TLatAndLon(TextualConvention, OctetString):
    description = "antenna latitude and longitude specification. field octets contents range ----- ------ -------- ----- 1 1 +/-180 deg '+' / '-' 2 2 degree 0..180 3 3 minute 0..59 4 4 second 0..59 5 5 second fraction 0..99 +/- dd:mm:ss.ss "
    status = 'current'
    displayHint = '1a1d:1d:1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(5, 5)
    fixedLength = 5

class TAntHeight(TextualConvention, OctetString):
    description = "antenna height specification. field octets contents range ----- ------ -------- ----- 1 1 +/- '+' / '-' 2 2-3 meter 0..10000 3 4 meter fraction 0..99 +/- hh.hh "
    status = 'current'
    displayHint = '1a2d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class TLocalTimeOffset(TextualConvention, OctetString):
    description = "A local time offset specification. field octets contents range ----- ------ -------- ----- 1 1 direction from UTC '+' / '-' 2 2 hours from UTC* 0..13 3 3 minutes from UTC 0..59 * Notes: - the value of year is in network-byte order - The hours range is 0..13 For example, the -6 local time offset would be displayed as: -6:0 "
    status = 'current'
    displayHint = '1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class TSsm(TextualConvention, Integer32):
    description = 'The ssm hex code'
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

entPhysicalExtTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1), )
if mibBuilder.loadTexts: entPhysicalExtTable.setStatus('current')
if mibBuilder.loadTexts: entPhysicalExtTable.setDescription('Physical entity extension from public ENTITY-MIB (RFC2737). This extension contains additional information for the module entry in the ENTITY-MIB.')
entPhysicalExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1), )
entPhysicalEntry.registerAugmentions(("SYMMENTITYPHYSICALEXT", "entPhysicalExtEntry"))
entPhysicalExtEntry.setIndexNames(*entPhysicalEntry.getIndexNames())
if mibBuilder.loadTexts: entPhysicalExtEntry.setStatus('current')
if mibBuilder.loadTexts: entPhysicalExtEntry.setDescription('An entry of the physical entity extension table. Each entry is for a module entry in the ENTITY-MIB. ')
entPhyInService = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhyInService.setStatus('current')
if mibBuilder.loadTexts: entPhyInService.setDescription('A DateAndTime string containing information about in-service time for the module.')
entPhyCLEINum = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhyCLEINum.setStatus('current')
if mibBuilder.loadTexts: entPhyCLEINum.setDescription('The current CLEI number is given, if one is assigned.')
entPhyFPGAVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhyFPGAVersion.setStatus('current')
if mibBuilder.loadTexts: entPhyFPGAVersion.setDescription('The current FPGA version is given.')
entPhySlot = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySlot.setStatus('current')
if mibBuilder.loadTexts: entPhySlot.setDescription('Position of the module in a chassis. ')
entPhyCompatiHW = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhyCompatiHW.setStatus('current')
if mibBuilder.loadTexts: entPhyCompatiHW.setDescription('The HW compatibility value. ')
entPhyCompatiSW = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhyCompatiSW.setStatus('current')
if mibBuilder.loadTexts: entPhyCompatiSW.setDescription('The SW compatibility value. ')
entPhyCompatiMtoM = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhyCompatiMtoM.setStatus('current')
if mibBuilder.loadTexts: entPhyCompatiMtoM.setDescription('The Module-to-Module compatibility value. ')
entPhyCountryOfOrigin = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhyCountryOfOrigin.setStatus('current')
if mibBuilder.loadTexts: entPhyCountryOfOrigin.setDescription('The Country of Origin of module')
entPhyManufacturerID = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhyManufacturerID.setStatus('current')
if mibBuilder.loadTexts: entPhyManufacturerID.setDescription('The Manufacturer ID of module. ')
entPhysicalExtConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 2))
if mibBuilder.loadTexts: entPhysicalExtConformance.setStatus('current')
if mibBuilder.loadTexts: entPhysicalExtConformance.setDescription('This subtree contains conformance statements for the symmEntityPhysicalExt MIB. ')
entPhysicalExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 2, 1))
entPhysicalExtBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 2, 1, 1)).setObjects(("SYMMENTITYPHYSICALEXT", "entPhysicalExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entPhysicalExtBasicCompliance = entPhysicalExtBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: entPhysicalExtBasicCompliance.setDescription('The compliance statement for SNMP entities which have physical entity extension.')
entPhysicalExtUocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 2, 2))
entPhysicalExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 2, 2, 1)).setObjects(("SYMMENTITYPHYSICALEXT", "entPhyInService"), ("SYMMENTITYPHYSICALEXT", "entPhyCLEINum"), ("SYMMENTITYPHYSICALEXT", "entPhyFPGAVersion"), ("SYMMENTITYPHYSICALEXT", "entPhySlot"), ("SYMMENTITYPHYSICALEXT", "entPhyCompatiHW"), ("SYMMENTITYPHYSICALEXT", "entPhyCompatiSW"), ("SYMMENTITYPHYSICALEXT", "entPhyCompatiMtoM"), ("SYMMENTITYPHYSICALEXT", "entPhyCountryOfOrigin"), ("SYMMENTITYPHYSICALEXT", "entPhyManufacturerID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entPhysicalExtGroup = entPhysicalExtGroup.setStatus('current')
if mibBuilder.loadTexts: entPhysicalExtGroup.setDescription('A collection of objects providing information applicable to physical entity extension group.')
mibBuilder.exportSymbols("SYMMENTITYPHYSICALEXT", TAntHeight=TAntHeight, entPhysicalExtTable=entPhysicalExtTable, entPhyCLEINum=entPhyCLEINum, entPhySlot=entPhySlot, PYSNMP_MODULE_ID=symmEntityPhysicalExt, TLatAndLon=TLatAndLon, entPhyCompatiSW=entPhyCompatiSW, entPhysicalExtBasicCompliance=entPhysicalExtBasicCompliance, entPhysicalExtGroup=entPhysicalExtGroup, entPhyInService=entPhyInService, entPhyCountryOfOrigin=entPhyCountryOfOrigin, entPhyCompatiMtoM=entPhyCompatiMtoM, entPhyManufacturerID=entPhyManufacturerID, TSsm=TSsm, entPhysicalExtUocGroups=entPhysicalExtUocGroups, DateAndTime=DateAndTime, entPhyCompatiHW=entPhyCompatiHW, TLocalTimeOffset=TLocalTimeOffset, entPhysicalExtConformance=entPhysicalExtConformance, entPhysicalExtEntry=entPhysicalExtEntry, symmEntityPhysicalExt=symmEntityPhysicalExt, entPhysicalExtCompliances=entPhysicalExtCompliances, entPhyFPGAVersion=entPhyFPGAVersion)
