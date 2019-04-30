#
# PySNMP MIB module BYTESPHERE-TRAPMGR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BYTESPHERE-TRAPMGR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:25:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
bytesphereMgmt, = mibBuilder.importSymbols("BYTESPHERE-SMI", "bytesphereMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, Integer32, Unsigned32, Counter64, TimeTicks, iso, Bits, Gauge32, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "Integer32", "Unsigned32", "Counter64", "TimeTicks", "iso", "Bits", "Gauge32", "NotificationType", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bytesphereTrapMgrMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 7013, 1, 2))
bytesphereTrapMgrMib.setRevisions(('2007-10-05 00:00',))
if mibBuilder.loadTexts: bytesphereTrapMgrMib.setLastUpdated('200710050000Z')
if mibBuilder.loadTexts: bytesphereTrapMgrMib.setOrganization('ByteSphere Technologies LLC')
bytesphereTrapMgrObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7013, 1, 2, 1))
trapMgrSourceHost = MibScalar((1, 3, 6, 1, 4, 1, 7013, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapMgrSourceHost.setStatus('current')
mibBuilder.exportSymbols("BYTESPHERE-TRAPMGR-MIB", PYSNMP_MODULE_ID=bytesphereTrapMgrMib, bytesphereTrapMgrObjects=bytesphereTrapMgrObjects, bytesphereTrapMgrMib=bytesphereTrapMgrMib, trapMgrSourceHost=trapMgrSourceHost)
