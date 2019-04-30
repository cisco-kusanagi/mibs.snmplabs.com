#
# PySNMP MIB module CISCO-APPNAV-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-APPNAV-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:32:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, Counter32, TimeTicks, Counter64, ObjectIdentity, Gauge32, Unsigned32, iso, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "Counter32", "TimeTicks", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "iso", "Integer32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoAppnavCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 610))
ciscoAppnavCapability.setRevisions(('2012-04-17 00:00',))
if mibBuilder.loadTexts: ciscoAppnavCapability.setLastUpdated('201204170000Z')
if mibBuilder.loadTexts: ciscoAppnavCapability.setOrganization('Cisco Systems, Inc.')
ciscoAppNavCapabilityWAASV5R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 610, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAppNavCapabilityWAASV5R0 = ciscoAppNavCapabilityWAASV5R0.setProductRelease('OS=WAAS\n                     OSVERSION=V501')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAppNavCapabilityWAASV5R0 = ciscoAppNavCapabilityWAASV5R0.setStatus('current')
mibBuilder.exportSymbols("CISCO-APPNAV-CAPABILITY", PYSNMP_MODULE_ID=ciscoAppnavCapability, ciscoAppNavCapabilityWAASV5R0=ciscoAppNavCapabilityWAASV5R0, ciscoAppnavCapability=ciscoAppnavCapability)
