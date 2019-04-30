#
# PySNMP MIB module CISCO-IP-FORWARD-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IP-FORWARD-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:44:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, ModuleIdentity, MibIdentifier, NotificationType, Gauge32, ObjectIdentity, Counter64, iso, Counter32, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "ModuleIdentity", "MibIdentifier", "NotificationType", "Gauge32", "ObjectIdentity", "Counter64", "iso", "Counter32", "IpAddress", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIpForwardCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 595))
ciscoIpForwardCapability.setRevisions(('2010-09-23 00:00',))
if mibBuilder.loadTexts: ciscoIpForwardCapability.setLastUpdated('201009230000Z')
if mibBuilder.loadTexts: ciscoIpForwardCapability.setOrganization('Cisco Systems, Inc.')
ciscoIpForwardCapabilityV12R2SE = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 595, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpForwardCapabilityV12R2SE = ciscoIpForwardCapabilityV12R2SE.setProductRelease('Cisco IOS 12.2SE Catalyst 2k/3k series.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpForwardCapabilityV12R2SE = ciscoIpForwardCapabilityV12R2SE.setStatus('current')
mibBuilder.exportSymbols("CISCO-IP-FORWARD-CAPABILITY", PYSNMP_MODULE_ID=ciscoIpForwardCapability, ciscoIpForwardCapability=ciscoIpForwardCapability, ciscoIpForwardCapabilityV12R2SE=ciscoIpForwardCapabilityV12R2SE)
