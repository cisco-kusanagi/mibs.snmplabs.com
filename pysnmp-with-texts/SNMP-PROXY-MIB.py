#
# PySNMP MIB module SNMP-PROXY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMP-PROXY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:08:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
SnmpEngineID, SnmpAdminString = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpEngineID", "SnmpAdminString")
SnmpTagValue, = mibBuilder.importSymbols("SNMP-TARGET-MIB", "SnmpTagValue")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, snmpModules, Counter32, Counter64, IpAddress, NotificationType, Bits, iso, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "snmpModules", "Counter32", "Counter64", "IpAddress", "NotificationType", "Bits", "iso", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "MibIdentifier", "Unsigned32")
DisplayString, TextualConvention, RowStatus, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "StorageType")
snmpProxyMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 14))
snmpProxyMIB.setRevisions(('2002-10-14 00:00', '1998-08-04 00:00', '1997-07-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snmpProxyMIB.setRevisionsDescriptions(('Clarifications, published as RFC 3413.', 'Clarifications, published as RFC 2573.', 'The initial revision, published as RFC2273.',))
if mibBuilder.loadTexts: snmpProxyMIB.setLastUpdated('200210140000Z')
if mibBuilder.loadTexts: snmpProxyMIB.setOrganization('IETF SNMPv3 Working Group')
if mibBuilder.loadTexts: snmpProxyMIB.setContactInfo('WG-email: snmpv3@lists.tislabs.com Subscribe: majordomo@lists.tislabs.com In message body: subscribe snmpv3 Co-Chair: Russ Mundy Network Associates Laboratories Postal: 15204 Omega Drive, Suite 300 Rockville, MD 20850-4601 USA EMail: mundy@tislabs.com Phone: +1 301-947-7107 Co-Chair: David Harrington Enterasys Networks Postal: 35 Industrial Way P. O. Box 5004 Rochester, New Hampshire 03866-5005 USA EMail: dbh@enterasys.com Phone: +1 603-337-2614 Co-editor: David B. Levi Nortel Networks Postal: 3505 Kesterwood Drive Knoxville, Tennessee 37918 EMail: dlevi@nortelnetworks.com Phone: +1 865 686 0432 Co-editor: Paul Meyer Secure Computing Corporation Postal: 2675 Long Lake Road Roseville, Minnesota 55113 EMail: paul_meyer@securecomputing.com Phone: +1 651 628 1592 Co-editor: Bob Stewart Retired')
if mibBuilder.loadTexts: snmpProxyMIB.setDescription('This MIB module defines MIB objects which provide mechanisms to remotely configure the parameters used by a proxy forwarding application. Copyright (C) The Internet Society (2002). This version of this MIB module is part of RFC 3413; see the RFC itself for full legal notices. ')
snmpProxyObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 14, 1))
snmpProxyConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 14, 3))
snmpProxyTable = MibTable((1, 3, 6, 1, 6, 3, 14, 1, 2), )
if mibBuilder.loadTexts: snmpProxyTable.setStatus('current')
if mibBuilder.loadTexts: snmpProxyTable.setDescription('The table of translation parameters used by proxy forwarder applications for forwarding SNMP messages.')
snmpProxyEntry = MibTableRow((1, 3, 6, 1, 6, 3, 14, 1, 2, 1), ).setIndexNames((1, "SNMP-PROXY-MIB", "snmpProxyName"))
if mibBuilder.loadTexts: snmpProxyEntry.setStatus('current')
if mibBuilder.loadTexts: snmpProxyEntry.setDescription('A set of translation parameters used by a proxy forwarder application for forwarding SNMP messages. Entries in the snmpProxyTable are created and deleted using the snmpProxyRowStatus object.')
snmpProxyName = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: snmpProxyName.setStatus('current')
if mibBuilder.loadTexts: snmpProxyName.setDescription('The locally arbitrary, but unique identifier associated with this snmpProxyEntry.')
snmpProxyType = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("read", 1), ("write", 2), ("trap", 3), ("inform", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxyType.setStatus('current')
if mibBuilder.loadTexts: snmpProxyType.setDescription('The type of message that may be forwarded using the translation parameters defined by this entry.')
snmpProxyContextEngineID = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 3), SnmpEngineID()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxyContextEngineID.setStatus('current')
if mibBuilder.loadTexts: snmpProxyContextEngineID.setDescription('The contextEngineID contained in messages that may be forwarded using the translation parameters defined by this entry.')
snmpProxyContextName = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 4), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxyContextName.setStatus('current')
if mibBuilder.loadTexts: snmpProxyContextName.setDescription('The contextName contained in messages that may be forwarded using the translation parameters defined by this entry. This object is optional, and if not supported, the contextName contained in a message is ignored when selecting an entry in the snmpProxyTable.')
snmpProxyTargetParamsIn = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 5), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxyTargetParamsIn.setStatus('current')
if mibBuilder.loadTexts: snmpProxyTargetParamsIn.setDescription('This object selects an entry in the snmpTargetParamsTable. The selected entry is used to determine which row of the snmpProxyTable to use for forwarding received messages.')
snmpProxySingleTargetOut = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 6), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxySingleTargetOut.setStatus('current')
if mibBuilder.loadTexts: snmpProxySingleTargetOut.setDescription('This object selects a management target defined in the snmpTargetAddrTable (in the SNMP-TARGET-MIB). The selected target is defined by an entry in the snmpTargetAddrTable whose index value (snmpTargetAddrName) is equal to this object. This object is only used when selection of a single target is required (i.e. when forwarding an incoming read or write request).')
snmpProxyMultipleTargetOut = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 7), SnmpTagValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxyMultipleTargetOut.setStatus('current')
if mibBuilder.loadTexts: snmpProxyMultipleTargetOut.setDescription('This object selects a set of management targets defined in the snmpTargetAddrTable (in the SNMP-TARGET-MIB). This object is only used when selection of multiple targets is required (i.e. when forwarding an incoming notification).')
snmpProxyStorageType = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 8), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxyStorageType.setStatus('current')
if mibBuilder.loadTexts: snmpProxyStorageType.setDescription("The storage type of this conceptual row. Conceptual rows having the value 'permanent' need not allow write-access to any columnar objects in the row.")
snmpProxyRowStatus = MibTableColumn((1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpProxyRowStatus.setStatus('current')
if mibBuilder.loadTexts: snmpProxyRowStatus.setDescription('The status of this conceptual row. To create a row in this table, a manager must set this object to either createAndGo(4) or createAndWait(5). The following objects may not be modified while the value of this object is active(1): - snmpProxyType - snmpProxyContextEngineID - snmpProxyContextName - snmpProxyTargetParamsIn - snmpProxySingleTargetOut - snmpProxyMultipleTargetOut')
snmpProxyCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 14, 3, 1))
snmpProxyGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 14, 3, 2))
snmpProxyCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 14, 3, 1, 1)).setObjects(("SNMP-TARGET-MIB", "snmpTargetBasicGroup"), ("SNMP-TARGET-MIB", "snmpTargetResponseGroup"), ("SNMP-PROXY-MIB", "snmpProxyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpProxyCompliance = snmpProxyCompliance.setStatus('current')
if mibBuilder.loadTexts: snmpProxyCompliance.setDescription('The compliance statement for SNMP entities which include a proxy forwarding application.')
snmpProxyGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 14, 3, 2, 3)).setObjects(("SNMP-PROXY-MIB", "snmpProxyType"), ("SNMP-PROXY-MIB", "snmpProxyContextEngineID"), ("SNMP-PROXY-MIB", "snmpProxyContextName"), ("SNMP-PROXY-MIB", "snmpProxyTargetParamsIn"), ("SNMP-PROXY-MIB", "snmpProxySingleTargetOut"), ("SNMP-PROXY-MIB", "snmpProxyMultipleTargetOut"), ("SNMP-PROXY-MIB", "snmpProxyStorageType"), ("SNMP-PROXY-MIB", "snmpProxyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpProxyGroup = snmpProxyGroup.setStatus('current')
if mibBuilder.loadTexts: snmpProxyGroup.setDescription('A collection of objects providing remote configuration of management target translation parameters for use by proxy forwarder applications.')
mibBuilder.exportSymbols("SNMP-PROXY-MIB", snmpProxyContextEngineID=snmpProxyContextEngineID, PYSNMP_MODULE_ID=snmpProxyMIB, snmpProxyCompliances=snmpProxyCompliances, snmpProxyMIB=snmpProxyMIB, snmpProxyRowStatus=snmpProxyRowStatus, snmpProxySingleTargetOut=snmpProxySingleTargetOut, snmpProxyGroup=snmpProxyGroup, snmpProxyTargetParamsIn=snmpProxyTargetParamsIn, snmpProxyEntry=snmpProxyEntry, snmpProxyType=snmpProxyType, snmpProxyContextName=snmpProxyContextName, snmpProxyMultipleTargetOut=snmpProxyMultipleTargetOut, snmpProxyTable=snmpProxyTable, snmpProxyStorageType=snmpProxyStorageType, snmpProxyGroups=snmpProxyGroups, snmpProxyCompliance=snmpProxyCompliance, snmpProxyName=snmpProxyName, snmpProxyObjects=snmpProxyObjects, snmpProxyConformance=snmpProxyConformance)