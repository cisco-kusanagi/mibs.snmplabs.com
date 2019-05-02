#
# PySNMP MIB module CAJUN-SWITCH-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CAJUN-SWITCH-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:46:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter32, NotificationType, ObjectIdentity, Unsigned32, TimeTicks, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, Bits, Integer32, enterprises, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "NotificationType", "ObjectIdentity", "Unsigned32", "TimeTicks", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "Bits", "Integer32", "enterprises", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lucent = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751))
if mibBuilder.loadTexts: lucent.setLastUpdated('9901300000Z')
if mibBuilder.loadTexts: lucent.setOrganization("Lucent's Concord Technology Center (CTC) ")
if mibBuilder.loadTexts: lucent.setContactInfo('Erick M. Crowell -- ecrowell@lucent.com, Raj Duggal -- rduggal@lucent.com, Ira Steckler -- isteckler@lucent.com')
if mibBuilder.loadTexts: lucent.setDescription('Cajun p220 / p550 / p660 / p880 Private Mib top level Architecture.')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1))
mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2))
cajunSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 45))
cajunSwitchProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 45))
cajunL2P550 = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 45, 1))
cajunL3P550 = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 45, 2))
cajunP220G = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 45, 3))
cajunP220FE = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 45, 4))
mibBuilder.exportSymbols("CAJUN-SWITCH-PRODUCTS-MIB", products=products, cajunL3P550=cajunL3P550, cajunSwitchProduct=cajunSwitchProduct, mibs=mibs, cajunP220G=cajunP220G, cajunP220FE=cajunP220FE, cajunSwitch=cajunSwitch, lucent=lucent, cajunL2P550=cajunL2P550, PYSNMP_MODULE_ID=lucent)
