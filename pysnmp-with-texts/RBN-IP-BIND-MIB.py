#
# PySNMP MIB module RBN-IP-BIND-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-IP-BIND-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:52:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
InterfaceIndexOrZero, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifIndex")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
RbnCircuitHandle, = mibBuilder.importSymbols("RBN-TC", "RbnCircuitHandle")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, ModuleIdentity, Counter64, NotificationType, MibIdentifier, iso, IpAddress, ObjectIdentity, Unsigned32, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "Counter64", "NotificationType", "MibIdentifier", "iso", "IpAddress", "ObjectIdentity", "Unsigned32", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbnIpBindMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 26))
rbnIpBindMib.setRevisions(('2002-08-20 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbnIpBindMib.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: rbnIpBindMib.setLastUpdated('200208201200Z')
if mibBuilder.loadTexts: rbnIpBindMib.setOrganization('Redback Networks, Inc.')
if mibBuilder.loadTexts: rbnIpBindMib.setContactInfo(' RedBack Networks, Inc. Postal: 300 Holger Way San Jose, CA 95134-1362 USA Phone: +1 408 750 5000 Fax: +1 408 750 5599 E-mail: mib-info@redback.com')
if mibBuilder.loadTexts: rbnIpBindMib.setDescription('The MIB module for monitoring IP interface binding to physical ports and circuits as they are represented in the IF-MIB.')
rbnIpBindMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 26, 0))
rbnIpBindMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 26, 1))
rbnIpBindMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 26, 2))
rbnIpBindTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 26, 1, 1), )
if mibBuilder.loadTexts: rbnIpBindTable.setStatus('current')
if mibBuilder.loadTexts: rbnIpBindTable.setDescription(' A table that shows IP interface bindings to physical ports and circuit encapsulation layers as they are represented in the IF-MIB. This table displays all IP interface bindings in all contexts but is only visible from the local context. ')
rbnIpBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 26, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "RBN-IP-BIND-MIB", "rbnIpBindCircuitHandle"))
if mibBuilder.loadTexts: rbnIpBindEntry.setStatus('current')
if mibBuilder.loadTexts: rbnIpBindEntry.setDescription('A conceptual row in the rbnIpBindTable. Each ifIndex instance that is included as an INDEX component represents an IP interface and has an ifType value of propVirtual. ')
rbnIpBindCircuitHandle = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 26, 1, 1, 1, 1), RbnCircuitHandle())
if mibBuilder.loadTexts: rbnIpBindCircuitHandle.setStatus('current')
if mibBuilder.loadTexts: rbnIpBindCircuitHandle.setDescription('A unique identifier for the circuit the IP interface is bound to. Note that the term circuit as defined in this table can represent a port, channel, subchannel or a virtual circuit configured to run over a port, channel or subchannel. ')
rbnIpBindIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 26, 1, 1, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnIpBindIfIndex.setStatus('current')
if mibBuilder.loadTexts: rbnIpBindIfIndex.setDescription('If the IP interface is bound to a port, channel, subchannel, or virtual circuit that is included in the IF-MIB, this object contains the ifIndex of that layer, otherwise this object is set to zero. ')
rbnIpBindHierarchicalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 26, 1, 1, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnIpBindHierarchicalIfIndex.setStatus('current')
if mibBuilder.loadTexts: rbnIpBindHierarchicalIfIndex.setDescription('If the IP interface is bound to a port, channel, subchannel, or virtual circuit that is not included in the IF-MIB, but that interface is part of a port stack that is included in the IF-MIB, this object contains the ifIndex of the port encapsulation layer that sits on top of that port stack. If rbnIpBindIfIndex is set to a non-zero value this object is set to zero. ')
rbnIpBindCircuitDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 26, 1, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 192))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnIpBindCircuitDescr.setStatus('current')
if mibBuilder.loadTexts: rbnIpBindCircuitDescr.setDescription('A descriptive version of rbnIpBindCircuitHandle that is consistent with information displayed in the CLI. On the SE router this string is formatted as slot/port:channel:subchannel authority/level/index, with the exception that channel and subchannel are only included when appropriate. For example, 4/1 1/2/7, 4/1:1 1/2/7 or 4/1:1:1 1/2/7. ')
rbnIpBindContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 26, 1, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnIpBindContextName.setStatus('current')
if mibBuilder.loadTexts: rbnIpBindContextName.setDescription('The name of the context in which this IP interface is defined.')
rbnIpBindCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 26, 2, 1))
rbnIpBindGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 26, 2, 2))
rbnIpBindCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 26, 2, 1, 1)).setObjects(("RBN-IP-BIND-MIB", "rbnIpBindDisplayGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnIpBindCompliance = rbnIpBindCompliance.setStatus('current')
if mibBuilder.loadTexts: rbnIpBindCompliance.setDescription('The compliance statement for SNMP entities which implement the RBN-IP-BIND-MIB.')
rbnIpBindDisplayGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 26, 2, 2, 1)).setObjects(("RBN-IP-BIND-MIB", "rbnIpBindIfIndex"), ("RBN-IP-BIND-MIB", "rbnIpBindHierarchicalIfIndex"), ("RBN-IP-BIND-MIB", "rbnIpBindCircuitDescr"), ("RBN-IP-BIND-MIB", "rbnIpBindContextName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnIpBindDisplayGroup = rbnIpBindDisplayGroup.setStatus('current')
if mibBuilder.loadTexts: rbnIpBindDisplayGroup.setDescription('A collection of objects that shows IP interface bindings to physical ports and circuits as represented in the IF-MIB.')
mibBuilder.exportSymbols("RBN-IP-BIND-MIB", rbnIpBindGroups=rbnIpBindGroups, rbnIpBindCircuitDescr=rbnIpBindCircuitDescr, rbnIpBindCompliance=rbnIpBindCompliance, rbnIpBindEntry=rbnIpBindEntry, rbnIpBindCircuitHandle=rbnIpBindCircuitHandle, rbnIpBindHierarchicalIfIndex=rbnIpBindHierarchicalIfIndex, rbnIpBindTable=rbnIpBindTable, rbnIpBindMibObjects=rbnIpBindMibObjects, rbnIpBindMibNotifications=rbnIpBindMibNotifications, rbnIpBindContextName=rbnIpBindContextName, rbnIpBindMibConformance=rbnIpBindMibConformance, rbnIpBindMib=rbnIpBindMib, rbnIpBindIfIndex=rbnIpBindIfIndex, rbnIpBindCompliances=rbnIpBindCompliances, rbnIpBindDisplayGroup=rbnIpBindDisplayGroup, PYSNMP_MODULE_ID=rbnIpBindMib)
