#
# PySNMP MIB module CISCO-SSL-PROXY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SSL-PROXY-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:56:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Counter64, IpAddress, Gauge32, Integer32, Bits, Counter32, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, NotificationType, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Gauge32", "Integer32", "Bits", "Counter32", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "NotificationType", "ObjectIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSslProxyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 364))
ciscoSslProxyCapability.setRevisions(('2008-04-08 00:00',))
if mibBuilder.loadTexts: ciscoSslProxyCapability.setLastUpdated('200804080000Z')
if mibBuilder.loadTexts: ciscoSslProxyCapability.setOrganization('Cisco Systems, Inc.')
ciscoSslProxyCapCat6KV02R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 364, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSslProxyCapCat6KV02R01 = ciscoSslProxyCapCat6KV02R01.setProductRelease('Cisco Catalyst 6000 SSL Module Release 2.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSslProxyCapCat6KV02R01 = ciscoSslProxyCapCat6KV02R01.setStatus('current')
ciscoSslProxyCapACSWV03RA3006 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 364, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSslProxyCapACSWV03RA3006 = ciscoSslProxyCapACSWV03RA3006.setProductRelease('ACSW (Application Control Software) 3.0(0)A3(0.0.6)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSslProxyCapACSWV03RA3006 = ciscoSslProxyCapACSWV03RA3006.setStatus('current')
mibBuilder.exportSymbols("CISCO-SSL-PROXY-CAPABILITY", ciscoSslProxyCapCat6KV02R01=ciscoSslProxyCapCat6KV02R01, PYSNMP_MODULE_ID=ciscoSslProxyCapability, ciscoSslProxyCapACSWV03RA3006=ciscoSslProxyCapACSWV03RA3006, ciscoSslProxyCapability=ciscoSslProxyCapability)
