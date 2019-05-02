#
# PySNMP MIB module MITEL-IPGROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-IPGROUP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:13:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, IpAddress, ObjectIdentity, NotificationType, Gauge32, Counter64, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, Bits, TimeTicks, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "IpAddress", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "Bits", "TimeTicks", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mitelRouterIpGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1))
mitelRouterIpGroup.setRevisions(('2003-03-24 09:08', '1999-03-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mitelRouterIpGroup.setRevisionsDescriptions(('Convert to SMIv2', 'IP MIB Version 1.0',))
if mibBuilder.loadTexts: mitelRouterIpGroup.setLastUpdated('200303240908Z')
if mibBuilder.loadTexts: mitelRouterIpGroup.setOrganization('MITEL Corporation')
if mibBuilder.loadTexts: mitelRouterIpGroup.setContactInfo('Standards Group, Postal: MITEL Corporation 350 Legget Drive, PO Box 13089 Kanata, Ontario Canada K2K 1X3 Tel: +1 613 592 2122 Fax: +1 613 592 4784 E-mail: std@mitel.com')
if mibBuilder.loadTexts: mitelRouterIpGroup.setDescription('The MITEL IP MIB module.')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelIpNetRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelIpGrpFilterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1))
mitelIpGrpNatGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2))
mitelIpGrpDnsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3))
mitelIpGrpIpVirtualGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4))
mitelIpGrpLogicalGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5))
mitelIpGrpBackupWANGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6))
mibBuilder.exportSymbols("MITEL-IPGROUP-MIB", mitelIpGrpIpVirtualGroup=mitelIpGrpIpVirtualGroup, mitelIpGrpFilterGroup=mitelIpGrpFilterGroup, mitelIpGrpNatGroup=mitelIpGrpNatGroup, mitelProprietary=mitelProprietary, mitelRouterIpGroup=mitelRouterIpGroup, mitelIpGrpDnsGroup=mitelIpGrpDnsGroup, mitelIpNetRouter=mitelIpNetRouter, mitelIpGrpBackupWANGroup=mitelIpGrpBackupWANGroup, PYSNMP_MODULE_ID=mitelRouterIpGroup, mitelIpGrpLogicalGroup=mitelIpGrpLogicalGroup, mitel=mitel, mitelPropIpNetworking=mitelPropIpNetworking)
