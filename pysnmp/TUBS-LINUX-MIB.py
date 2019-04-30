#
# PySNMP MIB module TUBS-LINUX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TUBS-LINUX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:20:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ModuleIdentity, Bits, iso, Gauge32, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Counter64, IpAddress, Integer32, enterprises, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "Bits", "iso", "Gauge32", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Counter64", "IpAddress", "Integer32", "enterprises", "Unsigned32")
RowStatus, TAddress, TimeStamp, TruthValue, TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TAddress", "TimeStamp", "TruthValue", "TextualConvention", "DateAndTime", "DisplayString")
linuxMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 5))
if mibBuilder.loadTexts: linuxMIB.setLastUpdated('9607152024Z')
if mibBuilder.loadTexts: linuxMIB.setOrganization('TU Braunschweig')
linuxAgents = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 5, 1))
linuxAgent3dot1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 1575, 1, 5, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    linuxAgent3dot1 = linuxAgent3dot1.setProductRelease('cmu-snmp-linux-3.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    linuxAgent3dot1 = linuxAgent3dot1.setStatus('current')
linuxMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 5, 2))
linuxCPU = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 5, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linuxCPU.setStatus('current')
linuxBogo = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 5, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linuxBogo.setStatus('current')
linuxMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 5, 3))
linuxMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 5, 3, 1))
linuxMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 5, 3, 2))
mibBuilder.exportSymbols("TUBS-LINUX-MIB", linuxMIBObjects=linuxMIBObjects, linuxCPU=linuxCPU, linuxAgents=linuxAgents, PYSNMP_MODULE_ID=linuxMIB, linuxBogo=linuxBogo, linuxMIBConformance=linuxMIBConformance, linuxMIBCompliances=linuxMIBCompliances, linuxAgent3dot1=linuxAgent3dot1, linuxMIB=linuxMIB, linuxMIBGroups=linuxMIBGroups)
