#
# PySNMP MIB module CISCO-SWITCH-RATE-LIMITER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SWITCH-RATE-LIMITER-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:57:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
iso, Integer32, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, Counter64, ObjectIdentity, IpAddress, ModuleIdentity, Counter32, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "ModuleIdentity", "Counter32", "Gauge32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSwitchRateLimiterCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 606))
ciscoSwitchRateLimiterCapability.setRevisions(('2011-07-27 00:00',))
if mibBuilder.loadTexts: ciscoSwitchRateLimiterCapability.setLastUpdated('201107270000Z')
if mibBuilder.loadTexts: ciscoSwitchRateLimiterCapability.setOrganization('Cisco Systems, Inc.')
ciscoRateLimiterCapNxOSV05R0201PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 606, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRateLimiterCapNxOSV05R0201PN7k = ciscoRateLimiterCapNxOSV05R0201PN7k.setProductRelease('Cisco NX-OS 5.2(1) on Nexus 7000\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRateLimiterCapNxOSV05R0201PN7k = ciscoRateLimiterCapNxOSV05R0201PN7k.setStatus('current')
mibBuilder.exportSymbols("CISCO-SWITCH-RATE-LIMITER-CAPABILITY", ciscoRateLimiterCapNxOSV05R0201PN7k=ciscoRateLimiterCapNxOSV05R0201PN7k, ciscoSwitchRateLimiterCapability=ciscoSwitchRateLimiterCapability, PYSNMP_MODULE_ID=ciscoSwitchRateLimiterCapability)
