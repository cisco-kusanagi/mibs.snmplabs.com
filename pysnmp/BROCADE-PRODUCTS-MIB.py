#
# PySNMP MIB module BROCADE-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BROCADE-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:24:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
bcsiReg, = mibBuilder.importSymbols("Brocade-REG-MIB", "bcsiReg")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibIdentifier, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, NotificationType, Bits, Unsigned32, ObjectIdentity, iso, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "NotificationType", "Bits", "Unsigned32", "ObjectIdentity", "iso", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
brocadeProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 3))
brocadeProductsMIB.setRevisions(('2012-02-03 00:00', '2013-11-21 00:00', '2013-09-25 13:00', '2014-10-07 14:05', '2015-08-11 13:05',))
if mibBuilder.loadTexts: brocadeProductsMIB.setLastUpdated('201202030000Z')
if mibBuilder.loadTexts: brocadeProductsMIB.setOrganization('Brocade Communications Systems, Inc.,')
brocadeProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1))
vdx6740 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 131))
vdx6740T = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 137))
vdx2740 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 138))
vdx6740T1G = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 151))
vdx6940Q36 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 153))
vdx6940S144 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 164))
vdx8770S4 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 1000))
vdx8770S8 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 1001))
vdx8770S16 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 3, 1, 1002))
mibBuilder.exportSymbols("BROCADE-PRODUCTS-MIB", vdx6740T=vdx6740T, brocadeProductsMIB=brocadeProductsMIB, brocadeProducts=brocadeProducts, vdx8770S4=vdx8770S4, vdx6740T1G=vdx6740T1G, PYSNMP_MODULE_ID=brocadeProductsMIB, vdx8770S16=vdx8770S16, vdx6940S144=vdx6940S144, vdx8770S8=vdx8770S8, vdx6940Q36=vdx6940Q36, vdx6740=vdx6740, vdx2740=vdx2740)
