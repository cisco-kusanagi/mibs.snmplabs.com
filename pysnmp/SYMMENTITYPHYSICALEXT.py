#
# PySNMP MIB module SYMMENTITYPHYSICALEXT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMENTITYPHYSICALEXT
# Produced by pysmi-0.3.4 at Tue Jul 30 11:34:21 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
entPhysicalIndex, entPhysicalEntry = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "entPhysicalEntry")
ifIndex, ifNumber = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifNumber")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, Bits, TimeTicks, NotificationType, MibIdentifier, Unsigned32, Integer32, Counter32, ModuleIdentity, Counter64, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "TimeTicks", "NotificationType", "MibIdentifier", "Unsigned32", "Integer32", "Counter32", "ModuleIdentity", "Counter64", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
symmEntPhysicalExtension, = mibBuilder.importSymbols("SYMM-COMMON-SMI", "symmEntPhysicalExtension")
symmEntityPhysicalExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1))
symmEntityPhysicalExt.setRevisions(('2016-06-15 10:39',))
if mibBuilder.loadTexts: symmEntityPhysicalExt.setLastUpdated('201606151039Z')
if mibBuilder.loadTexts: symmEntityPhysicalExt.setOrganization('Symmetricom')
class DateAndTime(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d:1d.1d,1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
class TLatAndLon(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a1d:1d:1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(5, 5)
    fixedLength = 5

class TAntHeight(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a2d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class TLocalTimeOffset(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class TSsm(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

entPhysicalExtTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1), )
if mibBuilder.loadTexts: entPhysicalExtTable.setStatus('current')
entPhysicalExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1), )
entPhysicalEntry.registerAugmentions(("SYMMENTITYPHYSICALEXT", "entPhysicalExtEntry"))
entPhysicalExtEntry.setIndexNames(*entPhysicalEntry.getIndexNames())
if mibBuilder.loadTexts: entPhysicalExtEntry.setStatus('current')
entPhyInService = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhyInService.setStatus('current')
entPhyCLEINum = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhyCLEINum.setStatus('current')
entPhyFPGAVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhyFPGAVersion.setStatus('current')
entPhySlot = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySlot.setStatus('current')
entPhyCompatiHW = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhyCompatiHW.setStatus('current')
entPhyCompatiSW = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhyCompatiSW.setStatus('current')
entPhyCompatiMtoM = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhyCompatiMtoM.setStatus('current')
entPhyCountryOfOrigin = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhyCountryOfOrigin.setStatus('current')
entPhyManufacturerID = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhyManufacturerID.setStatus('current')
entPhysicalExtConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 2))
if mibBuilder.loadTexts: entPhysicalExtConformance.setStatus('current')
entPhysicalExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 2, 1))
entPhysicalExtBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 2, 1, 1)).setObjects(("SYMMENTITYPHYSICALEXT", "entPhysicalExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entPhysicalExtBasicCompliance = entPhysicalExtBasicCompliance.setStatus('current')
entPhysicalExtUocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 2, 2))
entPhysicalExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 2, 2, 1)).setObjects(("SYMMENTITYPHYSICALEXT", "entPhyInService"), ("SYMMENTITYPHYSICALEXT", "entPhyCLEINum"), ("SYMMENTITYPHYSICALEXT", "entPhyFPGAVersion"), ("SYMMENTITYPHYSICALEXT", "entPhySlot"), ("SYMMENTITYPHYSICALEXT", "entPhyCompatiHW"), ("SYMMENTITYPHYSICALEXT", "entPhyCompatiSW"), ("SYMMENTITYPHYSICALEXT", "entPhyCompatiMtoM"), ("SYMMENTITYPHYSICALEXT", "entPhyCountryOfOrigin"), ("SYMMENTITYPHYSICALEXT", "entPhyManufacturerID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entPhysicalExtGroup = entPhysicalExtGroup.setStatus('current')
mibBuilder.exportSymbols("SYMMENTITYPHYSICALEXT", TLocalTimeOffset=TLocalTimeOffset, entPhySlot=entPhySlot, entPhyFPGAVersion=entPhyFPGAVersion, entPhysicalExtConformance=entPhysicalExtConformance, entPhysicalExtBasicCompliance=entPhysicalExtBasicCompliance, entPhyManufacturerID=entPhyManufacturerID, entPhyCompatiMtoM=entPhyCompatiMtoM, PYSNMP_MODULE_ID=symmEntityPhysicalExt, entPhyInService=entPhyInService, entPhysicalExtUocGroups=entPhysicalExtUocGroups, TSsm=TSsm, entPhyCompatiHW=entPhyCompatiHW, entPhysicalExtGroup=entPhysicalExtGroup, TLatAndLon=TLatAndLon, entPhyCLEINum=entPhyCLEINum, entPhysicalExtEntry=entPhysicalExtEntry, entPhyCompatiSW=entPhyCompatiSW, entPhysicalExtTable=entPhysicalExtTable, entPhysicalExtCompliances=entPhysicalExtCompliances, symmEntityPhysicalExt=symmEntityPhysicalExt, DateAndTime=DateAndTime, TAntHeight=TAntHeight, entPhyCountryOfOrigin=entPhyCountryOfOrigin)
