#
# PySNMP MIB module ELTEX-MES-AAA (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-AAA
# Produced by pysmi-0.3.4 at Mon Apr 29 18:46:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
eltMesRadius, eltMes = mibBuilder.importSymbols("ELTEX-MES", "eltMesRadius", "eltMes")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, Unsigned32, Integer32, Counter32, Counter64, NotificationType, iso, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "Unsigned32", "Integer32", "Counter32", "Counter64", "NotificationType", "iso", "IpAddress", "TimeTicks")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
eltMesAAA = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 79))
if mibBuilder.loadTexts: eltMesAAA.setLastUpdated('201509210000Z')
if mibBuilder.loadTexts: eltMesAAA.setOrganization('Eltex Ltd.')
class EltAAAMethodListModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("eltAAAMethodListModeTypeChain", 0), ("eltAAAMethodListModeTypeBreak", 1))

eltAAAMethodListMode = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 79, 1), EltAAAMethodListModeType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltAAAMethodListMode.setStatus('current')
eltMesRadiusAttr = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 80, 1))
eltRadiusAttrNasIdAccessEnable = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 80, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltRadiusAttrNasIdAccessEnable.setStatus('current')
eltRadiusAttrNasIdFormatString = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 80, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone('%h')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltRadiusAttrNasIdFormatString.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-AAA", eltRadiusAttrNasIdAccessEnable=eltRadiusAttrNasIdAccessEnable, eltAAAMethodListMode=eltAAAMethodListMode, eltMesRadiusAttr=eltMesRadiusAttr, PYSNMP_MODULE_ID=eltMesAAA, eltRadiusAttrNasIdFormatString=eltRadiusAttrNasIdFormatString, eltMesAAA=eltMesAAA, EltAAAMethodListModeType=EltAAAMethodListModeType)
