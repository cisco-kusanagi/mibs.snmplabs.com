#
# PySNMP MIB module SYMMOUTGEN (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMOUTGEN
# Produced by pysmi-0.3.4 at Tue Jul 30 11:34:28 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifNumber, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifNumber", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, Gauge32, Counter32, IpAddress, ObjectIdentity, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, Unsigned32, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Gauge32", "Counter32", "IpAddress", "ObjectIdentity", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "Unsigned32", "Bits", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
symmPhysicalSignal, = mibBuilder.importSymbols("SYMM-COMMON-SMI", "symmPhysicalSignal")
symmOutGen = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6))
symmOutGen.setRevisions(('2011-07-18 11:21',))
if mibBuilder.loadTexts: symmOutGen.setLastUpdated('201107181121Z')
if mibBuilder.loadTexts: symmOutGen.setOrganization('Symmetricom')
class GENERALOUTGENTYPE(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("squelch", 1), ("on", 2), ("ais", 3))

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

outGenStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 1))
outGenConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2))
outGenConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2, 1), )
if mibBuilder.loadTexts: outGenConfigTable.setStatus('current')
outGenConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SYMMOUTGEN", "outGenConfigIndex"))
if mibBuilder.loadTexts: outGenConfigEntry.setStatus('current')
outGenConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: outGenConfigIndex.setStatus('current')
outGenConfigWarmup = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2, 1, 1, 2), GENERALOUTGENTYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outGenConfigWarmup.setStatus('current')
outGenConfigFreerun = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2, 1, 1, 3), GENERALOUTGENTYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outGenConfigFreerun.setStatus('current')
outGenConfigHoldover = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2, 1, 1, 4), GENERALOUTGENTYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outGenConfigHoldover.setStatus('current')
outGenConfigFasttrack = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 2, 1, 1, 5), GENERALOUTGENTYPE()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outGenConfigFasttrack.setStatus('current')
outGenConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 3))
if mibBuilder.loadTexts: outGenConformance.setStatus('current')
outGenCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 3, 1))
outGenBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 3, 1, 1)).setObjects(("SYMMOUTGEN", "outGenGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    outGenBasicCompliance = outGenBasicCompliance.setStatus('current')
outGenUocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 3, 2))
outGenGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 2, 6, 3, 2, 1)).setObjects(("SYMMOUTGEN", "outGenConfigWarmup"), ("SYMMOUTGEN", "outGenConfigFreerun"), ("SYMMOUTGEN", "outGenConfigHoldover"), ("SYMMOUTGEN", "outGenConfigFasttrack"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    outGenGroup = outGenGroup.setStatus('current')
mibBuilder.exportSymbols("SYMMOUTGEN", outGenStatus=outGenStatus, outGenConfigIndex=outGenConfigIndex, outGenConfigWarmup=outGenConfigWarmup, PYSNMP_MODULE_ID=symmOutGen, DateAndTime=DateAndTime, outGenGroup=outGenGroup, outGenConfigFreerun=outGenConfigFreerun, TLocalTimeOffset=TLocalTimeOffset, outGenConfig=outGenConfig, TSsm=TSsm, outGenConfigFasttrack=outGenConfigFasttrack, symmOutGen=symmOutGen, outGenUocGroups=outGenUocGroups, outGenBasicCompliance=outGenBasicCompliance, TAntHeight=TAntHeight, outGenConfigTable=outGenConfigTable, GENERALOUTGENTYPE=GENERALOUTGENTYPE, outGenCompliances=outGenCompliances, TLatAndLon=TLatAndLon, outGenConfigHoldover=outGenConfigHoldover, outGenConformance=outGenConformance, outGenConfigEntry=outGenConfigEntry)
