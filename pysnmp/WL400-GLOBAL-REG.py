#
# PySNMP MIB module WL400-GLOBAL-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WL400-GLOBAL-REG
# Produced by pysmi-0.3.4 at Mon Apr 29 21:29:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, iso, Integer32, Gauge32, IpAddress, NotificationType, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Counter32, Counter64, Bits, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Integer32", "Gauge32", "IpAddress", "NotificationType", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Counter32", "Counter64", "Bits", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wl400GlobalRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 232, 143, 1, 1))
if mibBuilder.loadTexts: wl400GlobalRegModule.setLastUpdated('9905260000Z')
if mibBuilder.loadTexts: wl400GlobalRegModule.setOrganization('Compaq Computer Corporation')
compaq = MibIdentifier((1, 3, 6, 1, 4, 1, 232))
wl400Reg = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 143))
wl400Modules = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 143, 1))
wl400Generic = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 144))
wl400Products = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 145))
wl400Experimental = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 146))
wl400HAP = ObjectIdentity((1, 3, 6, 1, 4, 1, 232, 143, 7))
if mibBuilder.loadTexts: wl400HAP.setStatus('current')
mibBuilder.exportSymbols("WL400-GLOBAL-REG", wl400Reg=wl400Reg, compaq=compaq, wl400Products=wl400Products, wl400Modules=wl400Modules, PYSNMP_MODULE_ID=wl400GlobalRegModule, wl400GlobalRegModule=wl400GlobalRegModule, wl400HAP=wl400HAP, wl400Experimental=wl400Experimental, wl400Generic=wl400Generic)
