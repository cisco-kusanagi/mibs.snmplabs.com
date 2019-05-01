#
# PySNMP MIB module WL400-GLOBAL-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WL400-GLOBAL-REG
# Produced by pysmi-0.3.4 at Wed May  1 15:36:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Bits, Counter64, ObjectIdentity, iso, Integer32, Gauge32, Counter32, TimeTicks, ModuleIdentity, enterprises, MibIdentifier, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "Counter64", "ObjectIdentity", "iso", "Integer32", "Gauge32", "Counter32", "TimeTicks", "ModuleIdentity", "enterprises", "MibIdentifier", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wl400GlobalRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 232, 143, 1, 1))
if mibBuilder.loadTexts: wl400GlobalRegModule.setLastUpdated('9905260000Z')
if mibBuilder.loadTexts: wl400GlobalRegModule.setOrganization('Compaq Computer Corporation')
if mibBuilder.loadTexts: wl400GlobalRegModule.setContactInfo(' Name: Compaq Computer Corporation Address: 20555 SH 249 Zip: 77070 City: Houston Country: USA Phone: Fax: e-mail: ')
if mibBuilder.loadTexts: wl400GlobalRegModule.setDescription('The Compaq WL400 central registration module.')
compaq = MibIdentifier((1, 3, 6, 1, 4, 1, 232))
wl400Reg = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 143))
wl400Modules = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 143, 1))
wl400Generic = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 144))
wl400Products = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 145))
wl400Experimental = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 146))
wl400HAP = ObjectIdentity((1, 3, 6, 1, 4, 1, 232, 143, 7))
if mibBuilder.loadTexts: wl400HAP.setStatus('current')
if mibBuilder.loadTexts: wl400HAP.setDescription('WL400 Wireless HAP')
mibBuilder.exportSymbols("WL400-GLOBAL-REG", wl400GlobalRegModule=wl400GlobalRegModule, wl400Modules=wl400Modules, PYSNMP_MODULE_ID=wl400GlobalRegModule, wl400Generic=wl400Generic, compaq=compaq, wl400Products=wl400Products, wl400Experimental=wl400Experimental, wl400HAP=wl400HAP, wl400Reg=wl400Reg)
