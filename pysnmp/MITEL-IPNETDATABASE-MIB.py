#
# PySNMP MIB module MITEL-IPNETDATABASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-IPNET-DATABASE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:03:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, ObjectIdentity, Bits, NotificationType, IpAddress, Unsigned32, enterprises, ModuleIdentity, Gauge32, Counter32, MibIdentifier, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "ObjectIdentity", "Bits", "NotificationType", "IpAddress", "Unsigned32", "enterprises", "ModuleIdentity", "Gauge32", "Counter32", "MibIdentifier", "Counter64", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mitelRouterDatabaseVersion = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 8))
mitelRouterDatabaseVersion.setRevisions(('2003-03-24 09:26',))
if mibBuilder.loadTexts: mitelRouterDatabaseVersion.setLastUpdated('200303240926Z')
if mibBuilder.loadTexts: mitelRouterDatabaseVersion.setOrganization('MITEL Corporation')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelIpNetRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelRouterDatabaseMajorVersion = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelRouterDatabaseMajorVersion.setStatus('current')
mitelRouterDatabaseMinorVersion = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 8, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelRouterDatabaseMinorVersion.setStatus('current')
mibBuilder.exportSymbols("MITEL-IPNETDATABASE-MIB", mitelIpNetRouter=mitelIpNetRouter, mitelPropIpNetworking=mitelPropIpNetworking, PYSNMP_MODULE_ID=mitelRouterDatabaseVersion, mitelRouterDatabaseMinorVersion=mitelRouterDatabaseMinorVersion, mitelProprietary=mitelProprietary, mitel=mitel, mitelRouterDatabaseVersion=mitelRouterDatabaseVersion, mitelRouterDatabaseMajorVersion=mitelRouterDatabaseMajorVersion)
