#
# PySNMP MIB module CISCO-GPRS-CHARGING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-GPRS-CHARGING-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:59:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
NotificationType, ModuleIdentity, Counter32, Bits, IpAddress, Unsigned32, MibIdentifier, TimeTicks, iso, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Counter32", "Bits", "IpAddress", "Unsigned32", "MibIdentifier", "TimeTicks", "iso", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGprschargingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 297))
ciscoGprschargingCapability.setRevisions(('2004-02-03 22:30', '2003-04-08 17:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGprschargingCapability.setRevisionsDescriptions(('Added variations for cgprsCgAlarmHistType to cGprschargingCapabilityV12R2M8YW and also added a variations for new version cGprschargingCapabilityV12R3M2XB1', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGprschargingCapability.setLastUpdated('200402032230Z')
if mibBuilder.loadTexts: ciscoGprschargingCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGprschargingCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-gprs@cisco.com')
if mibBuilder.loadTexts: ciscoGprschargingCapability.setDescription('Agent capabilities for CISCO-GPRS-CHARGING-MIB')
cGprschargingCapabilityV12R2M8YD = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 297, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YD = cGprschargingCapabilityV12R2M8YD.setProductRelease('Cisco IOS 12.2(4)MX & 12.2(8)YD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YD = cGprschargingCapabilityV12R2M8YD.setStatus('current')
if mibBuilder.loadTexts: cGprschargingCapabilityV12R2M8YD.setDescription('Cisco GPRS CHARGING MIB capabilities.')
cGprschargingCapabilityV12R2M8YY1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 297, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YY1 = cGprschargingCapabilityV12R2M8YY1.setProductRelease('Cisco IOS 12.2(8)YY1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YY1 = cGprschargingCapabilityV12R2M8YY1.setStatus('current')
if mibBuilder.loadTexts: cGprschargingCapabilityV12R2M8YY1.setDescription('Cisco GPRS CHARGING MIB capabilities.')
cGprschargingCapabilityV12R2M8YW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 297, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YW = cGprschargingCapabilityV12R2M8YW.setProductRelease('Cisco IOS 12.2(8)YW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YW = cGprschargingCapabilityV12R2M8YW.setStatus('current')
if mibBuilder.loadTexts: cGprschargingCapabilityV12R2M8YW.setDescription('Cisco GPRS CHARGING MIB capabilities.')
cGprschargingCapabilityV12R3M2XB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 297, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R3M2XB1 = cGprschargingCapabilityV12R3M2XB1.setProductRelease('Cisco IOS 12.3(2)XB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R3M2XB1 = cGprschargingCapabilityV12R3M2XB1.setStatus('current')
if mibBuilder.loadTexts: cGprschargingCapabilityV12R3M2XB1.setDescription('Cisco GPRS CHARGING MIB capabilities.')
mibBuilder.exportSymbols("CISCO-GPRS-CHARGING-CAPABILITY", cGprschargingCapabilityV12R2M8YD=cGprschargingCapabilityV12R2M8YD, cGprschargingCapabilityV12R2M8YW=cGprschargingCapabilityV12R2M8YW, ciscoGprschargingCapability=ciscoGprschargingCapability, cGprschargingCapabilityV12R2M8YY1=cGprschargingCapabilityV12R2M8YY1, PYSNMP_MODULE_ID=ciscoGprschargingCapability, cGprschargingCapabilityV12R3M2XB1=cGprschargingCapabilityV12R3M2XB1)
