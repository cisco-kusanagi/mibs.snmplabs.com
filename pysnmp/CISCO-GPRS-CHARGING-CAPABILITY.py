#
# PySNMP MIB module CISCO-GPRS-CHARGING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-GPRS-CHARGING-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:42:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, Counter64, IpAddress, Counter32, TimeTicks, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, Bits, iso, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "IpAddress", "Counter32", "TimeTicks", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "Bits", "iso", "Gauge32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGprschargingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 297))
ciscoGprschargingCapability.setRevisions(('2004-02-03 22:30', '2003-04-08 17:30',))
if mibBuilder.loadTexts: ciscoGprschargingCapability.setLastUpdated('200402032230Z')
if mibBuilder.loadTexts: ciscoGprschargingCapability.setOrganization('Cisco Systems, Inc.')
cGprschargingCapabilityV12R2M8YD = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 297, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YD = cGprschargingCapabilityV12R2M8YD.setProductRelease('Cisco IOS 12.2(4)MX & 12.2(8)YD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YD = cGprschargingCapabilityV12R2M8YD.setStatus('current')
cGprschargingCapabilityV12R2M8YY1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 297, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YY1 = cGprschargingCapabilityV12R2M8YY1.setProductRelease('Cisco IOS 12.2(8)YY1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YY1 = cGprschargingCapabilityV12R2M8YY1.setStatus('current')
cGprschargingCapabilityV12R2M8YW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 297, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YW = cGprschargingCapabilityV12R2M8YW.setProductRelease('Cisco IOS 12.2(8)YW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R2M8YW = cGprschargingCapabilityV12R2M8YW.setStatus('current')
cGprschargingCapabilityV12R3M2XB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 297, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R3M2XB1 = cGprschargingCapabilityV12R3M2XB1.setProductRelease('Cisco IOS 12.3(2)XB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGprschargingCapabilityV12R3M2XB1 = cGprschargingCapabilityV12R3M2XB1.setStatus('current')
mibBuilder.exportSymbols("CISCO-GPRS-CHARGING-CAPABILITY", cGprschargingCapabilityV12R2M8YW=cGprschargingCapabilityV12R2M8YW, cGprschargingCapabilityV12R2M8YD=cGprschargingCapabilityV12R2M8YD, PYSNMP_MODULE_ID=ciscoGprschargingCapability, ciscoGprschargingCapability=ciscoGprschargingCapability, cGprschargingCapabilityV12R3M2XB1=cGprschargingCapabilityV12R3M2XB1, cGprschargingCapabilityV12R2M8YY1=cGprschargingCapabilityV12R2M8YY1)
