#
# PySNMP MIB module ALVARION-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:06:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alvarionProducts, alvarionModules = mibBuilder.importSymbols("ALVARION-SMI", "alvarionProducts", "alvarionModules")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, iso, ModuleIdentity, IpAddress, Counter32, MibIdentifier, NotificationType, Integer32, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "ModuleIdentity", "IpAddress", "Counter32", "MibIdentifier", "NotificationType", "Integer32", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alvarionProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 4, 2))
if mibBuilder.loadTexts: alvarionProductsMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionProductsMIB.setOrganization('Alvarion Ltd.')
alvarionWI2CTRL40 = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 25))
alvarionWI2CTRL200 = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 27))
alvarionWI2CTRL10 = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 35))
alvarionWI2SR1 = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 36))
alvarionWI2DR1 = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 37))
mibBuilder.exportSymbols("ALVARION-PRODUCTS-MIB", PYSNMP_MODULE_ID=alvarionProductsMIB, alvarionWI2CTRL200=alvarionWI2CTRL200, alvarionWI2CTRL40=alvarionWI2CTRL40, alvarionWI2SR1=alvarionWI2SR1, alvarionWI2CTRL10=alvarionWI2CTRL10, alvarionProductsMIB=alvarionProductsMIB, alvarionWI2DR1=alvarionWI2DR1)
