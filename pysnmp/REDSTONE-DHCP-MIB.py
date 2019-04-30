#
# PySNMP MIB module REDSTONE-DHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDSTONE-DHCP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:47:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
rsMgmt, = mibBuilder.importSymbols("REDSTONE-SMI", "rsMgmt")
RsEnable, = mibBuilder.importSymbols("REDSTONE-TC", "RsEnable")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, MibIdentifier, IpAddress, ModuleIdentity, iso, NotificationType, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, Integer32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "IpAddress", "ModuleIdentity", "iso", "NotificationType", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "Integer32", "Bits", "Gauge32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
rsDhcpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2773, 2, 22))
rsDhcpMIB.setRevisions(('1999-06-01 00:00',))
if mibBuilder.loadTexts: rsDhcpMIB.setLastUpdated('9906010000Z')
if mibBuilder.loadTexts: rsDhcpMIB.setOrganization('Redstone Communications Inc.')
rsDhcpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 22, 1))
rsDhcpRelay = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 22, 1, 1))
rsDhcpProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 22, 1, 2))
rsDhcpRelayScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 22, 1, 1, 1))
rsDhcpRelayAgentInfoEnable = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 22, 1, 1, 1, 1), RsEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsDhcpRelayAgentInfoEnable.setStatus('current')
rsDhcpRelayServerTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 22, 1, 1, 2), )
if mibBuilder.loadTexts: rsDhcpRelayServerTable.setStatus('current')
rsDhcpRelayServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 22, 1, 1, 2, 1), ).setIndexNames((0, "REDSTONE-DHCP-MIB", "rsDhcpRelayServerAddress"))
if mibBuilder.loadTexts: rsDhcpRelayServerEntry.setStatus('current')
rsDhcpRelayServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 22, 1, 1, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: rsDhcpRelayServerAddress.setStatus('current')
rsDhcpRelayServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 22, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsDhcpRelayServerRowStatus.setStatus('current')
rsDhcpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 22, 4))
rsDhcpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 22, 4, 1))
rsDhcpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 22, 4, 2))
rsDhcpRelayCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2773, 2, 22, 4, 1, 1)).setObjects(("REDSTONE-DHCP-MIB", "rsDhcpRelayGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsDhcpRelayCompliance = rsDhcpRelayCompliance.setStatus('current')
rsDhcpRelayGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 22, 4, 2, 1)).setObjects(("REDSTONE-DHCP-MIB", "rsDhcpRelayAgentInfoEnable"), ("REDSTONE-DHCP-MIB", "rsDhcpRelayServerRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsDhcpRelayGroup = rsDhcpRelayGroup.setStatus('current')
mibBuilder.exportSymbols("REDSTONE-DHCP-MIB", rsDhcpProxy=rsDhcpProxy, rsDhcpMIB=rsDhcpMIB, rsDhcpMIBConformance=rsDhcpMIBConformance, rsDhcpObjects=rsDhcpObjects, rsDhcpRelayAgentInfoEnable=rsDhcpRelayAgentInfoEnable, rsDhcpMIBCompliances=rsDhcpMIBCompliances, rsDhcpRelayCompliance=rsDhcpRelayCompliance, rsDhcpRelayScalars=rsDhcpRelayScalars, rsDhcpRelayServerAddress=rsDhcpRelayServerAddress, rsDhcpMIBGroups=rsDhcpMIBGroups, rsDhcpRelayGroup=rsDhcpRelayGroup, PYSNMP_MODULE_ID=rsDhcpMIB, rsDhcpRelayServerEntry=rsDhcpRelayServerEntry, rsDhcpRelay=rsDhcpRelay, rsDhcpRelayServerTable=rsDhcpRelayServerTable, rsDhcpRelayServerRowStatus=rsDhcpRelayServerRowStatus)
