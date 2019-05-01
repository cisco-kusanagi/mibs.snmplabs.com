#
# PySNMP MIB module MITEL-IPNETDATABASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-IPNET-DATABASE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:13:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Integer32, Counter64, Gauge32, enterprises, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, ObjectIdentity, MibIdentifier, TimeTicks, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Counter64", "Gauge32", "enterprises", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "TimeTicks", "Bits", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mitelRouterDatabaseVersion = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 8))
mitelRouterDatabaseVersion.setRevisions(('2003-03-24 09:26',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mitelRouterDatabaseVersion.setRevisionsDescriptions(('Initial Version',))
if mibBuilder.loadTexts: mitelRouterDatabaseVersion.setLastUpdated('200303240926Z')
if mibBuilder.loadTexts: mitelRouterDatabaseVersion.setOrganization('MITEL Corporation')
if mibBuilder.loadTexts: mitelRouterDatabaseVersion.setContactInfo('Standards Group, Postal: MITEL Corporation 350 Legget Drive, PO Box 13089 Kanata, Ontario Canada K2K 1X3 Tel: +1 613 592 2122 Fax: +1 613 592 4784 E-mail: std@mitel.com')
if mibBuilder.loadTexts: mitelRouterDatabaseVersion.setDescription('The MITEL IP Net Router MIB module.')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelIpNetRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelRouterDatabaseMajorVersion = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelRouterDatabaseMajorVersion.setStatus('current')
if mibBuilder.loadTexts: mitelRouterDatabaseMajorVersion.setDescription('Major version of the IP Networking database')
mitelRouterDatabaseMinorVersion = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 8, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelRouterDatabaseMinorVersion.setStatus('current')
if mibBuilder.loadTexts: mitelRouterDatabaseMinorVersion.setDescription('Minor version of the IP Networking database')
mibBuilder.exportSymbols("MITEL-IPNETDATABASE-MIB", mitelProprietary=mitelProprietary, PYSNMP_MODULE_ID=mitelRouterDatabaseVersion, mitelPropIpNetworking=mitelPropIpNetworking, mitelIpNetRouter=mitelIpNetRouter, mitel=mitel, mitelRouterDatabaseVersion=mitelRouterDatabaseVersion, mitelRouterDatabaseMinorVersion=mitelRouterDatabaseMinorVersion, mitelRouterDatabaseMajorVersion=mitelRouterDatabaseMajorVersion)
