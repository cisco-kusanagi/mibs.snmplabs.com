#
# PySNMP MIB module ELTEX-MES-AAA (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-AAA
# Produced by pysmi-0.3.4 at Wed May  1 13:00:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
eltMesRadius, eltMes = mibBuilder.importSymbols("ELTEX-MES", "eltMesRadius", "eltMes")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, ModuleIdentity, Integer32, IpAddress, Counter32, iso, Unsigned32, Bits, NotificationType, TimeTicks, MibIdentifier, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "Integer32", "IpAddress", "Counter32", "iso", "Unsigned32", "Bits", "NotificationType", "TimeTicks", "MibIdentifier", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
eltMesAAA = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 79))
if mibBuilder.loadTexts: eltMesAAA.setLastUpdated('201509210000Z')
if mibBuilder.loadTexts: eltMesAAA.setOrganization('Eltex Ltd.')
if mibBuilder.loadTexts: eltMesAAA.setContactInfo('http://www.eltex.nsk.ru')
if mibBuilder.loadTexts: eltMesAAA.setDescription('The private MIB module definition for Authentication, Authorization and Accounting in Eltex MES devices.')
class EltAAAMethodListModeType(TextualConvention, Integer32):
    description = 'Authentication mode type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("eltAAAMethodListModeTypeChain", 0), ("eltAAAMethodListModeTypeBreak", 1))

eltAAAMethodListMode = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 79, 1), EltAAAMethodListModeType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltAAAMethodListMode.setStatus('current')
if mibBuilder.loadTexts: eltAAAMethodListMode.setDescription('Specify the authentication mode.')
eltMesRadiusAttr = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 80, 1))
eltRadiusAttrNasIdAccessEnable = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 80, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltRadiusAttrNasIdAccessEnable.setStatus('current')
if mibBuilder.loadTexts: eltRadiusAttrNasIdAccessEnable.setDescription('Enable or disable including NAS-Identifier attribute in Access Request messages')
eltRadiusAttrNasIdFormatString = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 80, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone('%h')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltRadiusAttrNasIdFormatString.setStatus('current')
if mibBuilder.loadTexts: eltRadiusAttrNasIdFormatString.setDescription('The format string for NAS-Identifier RADIUS attribute.')
mibBuilder.exportSymbols("ELTEX-MES-AAA", eltMesRadiusAttr=eltMesRadiusAttr, eltMesAAA=eltMesAAA, eltRadiusAttrNasIdFormatString=eltRadiusAttrNasIdFormatString, PYSNMP_MODULE_ID=eltMesAAA, eltAAAMethodListMode=eltAAAMethodListMode, EltAAAMethodListModeType=EltAAAMethodListModeType, eltRadiusAttrNasIdAccessEnable=eltRadiusAttrNasIdAccessEnable)
