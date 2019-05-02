#
# PySNMP MIB module BROCADE-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BROCADE-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:41:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
bcsiReg, = mibBuilder.importSymbols("Brocade-REG-MIB", "bcsiReg")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter32, MibIdentifier, Integer32, iso, ModuleIdentity, IpAddress, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "MibIdentifier", "Integer32", "iso", "ModuleIdentity", "IpAddress", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "ObjectIdentity", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
brocadeProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 3))
brocadeProductsMIB.setRevisions(('2012-02-03 00:00', '2013-11-21 00:00', '2013-09-25 13:00', '2014-10-07 14:05', '2015-08-11 13:05',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: brocadeProductsMIB.setRevisionsDescriptions(('Initial version of this MIB module.', 'Updated name for Blackbird as vdx2740', 'Added new product name for Draco-T platform.', 'Added product name for RIGEL1U as vdx7770P36 and RIGEL2U as vdx7770P72.', 'Updated the product name for RIGEL1U as vdx6940Q36. then added RIGELMOR product name as vdx6940S144 and Removed RIGEL2U platform',))
if mibBuilder.loadTexts: brocadeProductsMIB.setLastUpdated('201202030000Z')
if mibBuilder.loadTexts: brocadeProductsMIB.setOrganization('Brocade Communications Systems, Inc.,')
if mibBuilder.loadTexts: brocadeProductsMIB.setContactInfo('Brocade Communications Systems, Inc. Postal: 130 Holger Way San Jose, CA 95134 U.S.A Tel: +1-408-333-8000 E-mail: support@Brocade.com web: www.brocade.com.')
if mibBuilder.loadTexts: brocadeProductsMIB.setDescription("This MIB module is for defining all the object identifiers to identify various hardware platforms. These identifiers are used as value for 'sysObjectID'.")
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
mibBuilder.exportSymbols("BROCADE-PRODUCTS-MIB", PYSNMP_MODULE_ID=brocadeProductsMIB, vdx6940S144=vdx6940S144, vdx6740T=vdx6740T, vdx6940Q36=vdx6940Q36, vdx8770S4=vdx8770S4, vdx6740=vdx6740, vdx6740T1G=vdx6740T1G, vdx8770S16=vdx8770S16, vdx2740=vdx2740, vdx8770S8=vdx8770S8, brocadeProducts=brocadeProducts, brocadeProductsMIB=brocadeProductsMIB)
