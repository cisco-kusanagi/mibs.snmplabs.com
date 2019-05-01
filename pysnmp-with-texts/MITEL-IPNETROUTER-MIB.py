#
# PySNMP MIB module MITEL-IPNETROUTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-IPNETROUTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:13:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, enterprises, Bits, iso, Counter32, NotificationType, Counter64, Unsigned32, IpAddress, MibIdentifier, Integer32, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "enterprises", "Bits", "iso", "Counter32", "NotificationType", "Counter64", "Unsigned32", "IpAddress", "MibIdentifier", "Integer32", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mitelIpNetRouter = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelIpNetRouter.setRevisions(('2003-03-24 09:27', '1999-03-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mitelIpNetRouter.setRevisionsDescriptions(('Convert to SMIv2', 'IP Router MIB Version 1.0',))
if mibBuilder.loadTexts: mitelIpNetRouter.setLastUpdated('200303240927Z')
if mibBuilder.loadTexts: mitelIpNetRouter.setOrganization('MITEL Corporation')
if mibBuilder.loadTexts: mitelIpNetRouter.setContactInfo('Standards Group, Postal: MITEL Corporation 350 Legget Drive, PO Box 13089 Kanata, Ontario Canada K2K 1X3 Tel: +1 613 592 2122 Fax: +1 613 592 4784 E-mail: std@mitel.com')
if mibBuilder.loadTexts: mitelIpNetRouter.setDescription('The MITEL IP Net Router MIB module.')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelRouterIpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1))
mitelRouterPppGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2))
mitelRouterDhcpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3))
mitelRouterLogicalGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4))
mitelRouterIpRouterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5))
mitelRouterRipExtensionGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 6))
mitelRouterSnmpTrapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 7))
mibBuilder.exportSymbols("MITEL-IPNETROUTER-MIB", mitelRouterPppGroup=mitelRouterPppGroup, mitelRouterLogicalGroup=mitelRouterLogicalGroup, mitelRouterSnmpTrapGroup=mitelRouterSnmpTrapGroup, mitelRouterIpRouterGroup=mitelRouterIpRouterGroup, mitelProprietary=mitelProprietary, mitelRouterRipExtensionGroup=mitelRouterRipExtensionGroup, mitelPropIpNetworking=mitelPropIpNetworking, mitel=mitel, mitelRouterDhcpGroup=mitelRouterDhcpGroup, mitelIpNetRouter=mitelIpNetRouter, PYSNMP_MODULE_ID=mitelIpNetRouter, mitelRouterIpGroup=mitelRouterIpGroup)
