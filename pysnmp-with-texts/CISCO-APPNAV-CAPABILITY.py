#
# PySNMP MIB module CISCO-APPNAV-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-APPNAV-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:50:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Unsigned32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, NotificationType, Counter64, Integer32, TimeTicks, Gauge32, iso, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "NotificationType", "Counter64", "Integer32", "TimeTicks", "Gauge32", "iso", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoAppnavCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 610))
ciscoAppnavCapability.setRevisions(('2012-04-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAppnavCapability.setRevisionsDescriptions(('Latest version of this MIB module.',))
if mibBuilder.loadTexts: ciscoAppnavCapability.setLastUpdated('201204170000Z')
if mibBuilder.loadTexts: ciscoAppnavCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAppnavCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-<list>@cisco.com')
if mibBuilder.loadTexts: ciscoAppnavCapability.setDescription('Agent capabilities for CISCO-APPNAV-MIB.')
ciscoAppNavCapabilityWAASV5R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 610, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAppNavCapabilityWAASV5R0 = ciscoAppNavCapabilityWAASV5R0.setProductRelease('OS=WAAS\n                     OSVERSION=V501')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAppNavCapabilityWAASV5R0 = ciscoAppNavCapabilityWAASV5R0.setStatus('current')
if mibBuilder.loadTexts: ciscoAppNavCapabilityWAASV5R0.setDescription('CISCO-APPNAV-MIB capabilities')
mibBuilder.exportSymbols("CISCO-APPNAV-CAPABILITY", PYSNMP_MODULE_ID=ciscoAppnavCapability, ciscoAppnavCapability=ciscoAppnavCapability, ciscoAppNavCapabilityWAASV5R0=ciscoAppNavCapabilityWAASV5R0)
