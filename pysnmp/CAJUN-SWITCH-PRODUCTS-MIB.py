#
# PySNMP MIB module CAJUN-SWITCH-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CAJUN-SWITCH-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:29:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter32, enterprises, ModuleIdentity, NotificationType, iso, Bits, ObjectIdentity, Unsigned32, IpAddress, MibIdentifier, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "enterprises", "ModuleIdentity", "NotificationType", "iso", "Bits", "ObjectIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lucent = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751))
if mibBuilder.loadTexts: lucent.setLastUpdated('9901300000Z')
if mibBuilder.loadTexts: lucent.setOrganization("Lucent's Concord Technology Center (CTC) ")
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1))
mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2))
cajunSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 45))
cajunSwitchProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 45))
cajunL2P550 = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 45, 1))
cajunL3P550 = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 45, 2))
cajunP220G = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 45, 3))
cajunP220FE = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 45, 4))
mibBuilder.exportSymbols("CAJUN-SWITCH-PRODUCTS-MIB", mibs=mibs, cajunL3P550=cajunL3P550, cajunP220FE=cajunP220FE, cajunSwitchProduct=cajunSwitchProduct, cajunSwitch=cajunSwitch, lucent=lucent, products=products, cajunP220G=cajunP220G, PYSNMP_MODULE_ID=lucent, cajunL2P550=cajunL2P550)
