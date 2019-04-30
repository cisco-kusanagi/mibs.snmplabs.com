#
# PySNMP MIB module EdgeSwitch-SFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EdgeSwitch-SFLOW-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:56:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
fastPath, = mibBuilder.importSymbols("EdgeSwitch-REF-MIB", "fastPath")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, ModuleIdentity, Counter32, Gauge32, ObjectIdentity, Unsigned32, Bits, Counter64, IpAddress, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "ModuleIdentity", "Counter32", "Gauge32", "ObjectIdentity", "Unsigned32", "Bits", "Counter64", "IpAddress", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fastPathSflow = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 1, 1, 59))
if mibBuilder.loadTexts: fastPathSflow.setLastUpdated('201201120000Z')
if mibBuilder.loadTexts: fastPathSflow.setOrganization('Broadcom Inc')
agentFastPathSflowObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 59, 1))
agentSflowSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 59, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSflowSourceInterface.setStatus('current')
mibBuilder.exportSymbols("EdgeSwitch-SFLOW-MIB", agentSflowSourceInterface=agentSflowSourceInterface, agentFastPathSflowObjects=agentFastPathSflowObjects, fastPathSflow=fastPathSflow, PYSNMP_MODULE_ID=fastPathSflow)
