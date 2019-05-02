#
# PySNMP MIB module ALVARION-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:22:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alvarionProducts, alvarionModules = mibBuilder.importSymbols("ALVARION-SMI", "alvarionProducts", "alvarionModules")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, TimeTicks, ModuleIdentity, Unsigned32, IpAddress, NotificationType, Bits, Counter32, MibIdentifier, Counter64, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "TimeTicks", "ModuleIdentity", "Unsigned32", "IpAddress", "NotificationType", "Bits", "Counter32", "MibIdentifier", "Counter64", "iso", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alvarionProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 4, 2))
if mibBuilder.loadTexts: alvarionProductsMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionProductsMIB.setOrganization('Alvarion Ltd.')
if mibBuilder.loadTexts: alvarionProductsMIB.setContactInfo('Alvarion Ltd. Postal: 21a HaBarzel St. P.O. Box 13139 Tel-Aviv 69710 Israel Phone: +972 3 645 6262')
if mibBuilder.loadTexts: alvarionProductsMIB.setDescription('Alvarion Product Identifiers.')
alvarionWI2CTRL40 = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 25))
alvarionWI2CTRL200 = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 27))
alvarionWI2CTRL10 = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 35))
alvarionWI2SR1 = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 36))
alvarionWI2DR1 = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 37))
mibBuilder.exportSymbols("ALVARION-PRODUCTS-MIB", alvarionWI2CTRL40=alvarionWI2CTRL40, PYSNMP_MODULE_ID=alvarionProductsMIB, alvarionWI2CTRL10=alvarionWI2CTRL10, alvarionWI2DR1=alvarionWI2DR1, alvarionWI2SR1=alvarionWI2SR1, alvarionWI2CTRL200=alvarionWI2CTRL200, alvarionProductsMIB=alvarionProductsMIB)
