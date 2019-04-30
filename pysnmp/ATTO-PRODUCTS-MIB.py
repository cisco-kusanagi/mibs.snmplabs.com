#
# PySNMP MIB module ATTO-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATTO-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:15:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, IpAddress, Integer32, Counter64, Unsigned32, Counter32, ObjectIdentity, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, enterprises, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "Integer32", "Counter64", "Unsigned32", "Counter32", "ObjectIdentity", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "enterprises", "MibIdentifier", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
attoProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4547, 3, 2))
attoProductsMIB.setRevisions(('2013-04-19 13:45',))
if mibBuilder.loadTexts: attoProductsMIB.setLastUpdated('201304191345Z')
if mibBuilder.loadTexts: attoProductsMIB.setOrganization('ATTO Technology, Inc.')
attotech = MibIdentifier((1, 3, 6, 1, 4, 1, 4547))
attoProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 1))
attoMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 2))
attoModules = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 3))
attoAgentCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 4))
attoGenericDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 1, 1))
attoHba = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 1, 3))
attoFB6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 1, 4))
attoFB6500N = MibIdentifier((1, 3, 6, 1, 4, 1, 4547, 1, 5))
mibBuilder.exportSymbols("ATTO-PRODUCTS-MIB", attoAgentCapability=attoAgentCapability, attoFB6500N=attoFB6500N, attoHba=attoHba, attoGenericDevice=attoGenericDevice, attotech=attotech, attoMgmt=attoMgmt, PYSNMP_MODULE_ID=attoProductsMIB, attoProducts=attoProducts, attoFB6500=attoFB6500, attoProductsMIB=attoProductsMIB, attoModules=attoModules)
