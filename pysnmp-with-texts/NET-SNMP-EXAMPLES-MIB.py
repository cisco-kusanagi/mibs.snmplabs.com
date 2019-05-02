#
# PySNMP MIB module NET-SNMP-EXAMPLES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NET-SNMP-EXAMPLES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:18:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
netSnmp, = mibBuilder.importSymbols("NET-SNMP-MIB", "netSnmp")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, TimeTicks, ModuleIdentity, Counter64, NotificationType, ObjectIdentity, IpAddress, Gauge32, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "TimeTicks", "ModuleIdentity", "Counter64", "NotificationType", "ObjectIdentity", "IpAddress", "Gauge32", "Unsigned32", "Bits")
StorageType, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "DisplayString", "TextualConvention", "RowStatus")
netSnmpExamples = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072, 2))
netSnmpExamples.setRevisions(('2004-06-15 00:00', '2002-02-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: netSnmpExamples.setRevisionsDescriptions(('Corrected notification example definitions', 'First draft',))
if mibBuilder.loadTexts: netSnmpExamples.setLastUpdated('200406150000Z')
if mibBuilder.loadTexts: netSnmpExamples.setOrganization('www.net-snmp.org')
if mibBuilder.loadTexts: netSnmpExamples.setContactInfo('postal: Wes Hardaker P.O. Box 382 Davis CA 95617 email: net-snmp-coders@lists.sourceforge.net')
if mibBuilder.loadTexts: netSnmpExamples.setDescription('Example MIB objects for agent module example implementations')
netSnmpExampleScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 2, 1))
netSnmpExampleTables = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 2, 2))
netSnmpExampleNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 2, 3))
netSnmpExampleNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 2, 3, 0))
netSnmpExampleNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 2, 3, 2))
netSnmpExampleInteger = MibScalar((1, 3, 6, 1, 4, 1, 8072, 2, 1, 1), Integer32().clone(42)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netSnmpExampleInteger.setStatus('current')
if mibBuilder.loadTexts: netSnmpExampleInteger.setDescription("This is a simple object which merely houses a writable integer. It's only purposes is to hold the value of a single integer. Writing to it will simply change the value for subsequent GET/GETNEXT/GETBULK retrievals. This example object is implemented in the agent/mibgroup/examples/scalar_int.c file.")
netSnmpExampleSleeper = MibScalar((1, 3, 6, 1, 4, 1, 8072, 2, 1, 2), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netSnmpExampleSleeper.setStatus('current')
if mibBuilder.loadTexts: netSnmpExampleSleeper.setDescription("This is a simple object which is a basic integer. It's value indicates the number of seconds that the agent will take in responding to requests of this object. This is implemented in a way which will allow the agent to keep responding to other requests while access to this object is blocked. It is writable, and changing it's value will change the amount of time the agent will effectively wait for before returning a response when this object is manipulated. Note that SET requests through this object will take longer, since the delay is applied to each internal transaction phase, which could result in delays of up to 4 times the value of this object. This example object is implemented in the agent/mibgroup/examples/delayed_instance.c file.")
netSnmpExampleString = MibScalar((1, 3, 6, 1, 4, 1, 8072, 2, 1, 3), SnmpAdminString().clone('So long, and thanks for all the fish!')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netSnmpExampleString.setStatus('current')
if mibBuilder.loadTexts: netSnmpExampleString.setDescription("This is a simple object which merely houses a writable string. It's only purposes is to hold the value of a single string. Writing to it will simply change the value for subsequent GET/GETNEXT/GETBULK retrievals. This example object is implemented in the agent/mibgroup/examples/watched.c file.")
netSnmpIETFWGTable = MibTable((1, 3, 6, 1, 4, 1, 8072, 2, 2, 1), )
if mibBuilder.loadTexts: netSnmpIETFWGTable.setStatus('current')
if mibBuilder.loadTexts: netSnmpIETFWGTable.setDescription('This table merely contains a set of data which is otherwise useless for true network management. It is a table which describes properies about a IETF Working Group, such as the names of the two working group chairs. This example table is implemented in the agent/mibgroup/examples/data_set.c file.')
netSnmpIETFWGEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8072, 2, 2, 1, 1), ).setIndexNames((0, "NET-SNMP-EXAMPLES-MIB", "nsIETFWGName"))
if mibBuilder.loadTexts: netSnmpIETFWGEntry.setStatus('current')
if mibBuilder.loadTexts: netSnmpIETFWGEntry.setDescription('A row describing a given working group')
nsIETFWGName = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 2, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: nsIETFWGName.setStatus('current')
if mibBuilder.loadTexts: nsIETFWGName.setDescription('The name of the IETF Working Group this table describes.')
nsIETFWGChair1 = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 2, 2, 1, 1, 2), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsIETFWGChair1.setStatus('current')
if mibBuilder.loadTexts: nsIETFWGChair1.setDescription('One of the names of the chairs for the IETF working group.')
nsIETFWGChair2 = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 2, 2, 1, 1, 3), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsIETFWGChair2.setStatus('current')
if mibBuilder.loadTexts: nsIETFWGChair2.setDescription('The other name, if one exists, of the chairs for the IETF working group.')
netSnmpHostsTable = MibTable((1, 3, 6, 1, 4, 1, 8072, 2, 2, 2), )
if mibBuilder.loadTexts: netSnmpHostsTable.setStatus('current')
if mibBuilder.loadTexts: netSnmpHostsTable.setDescription('An example table that implements a wrapper around the /etc/hosts file on a machine using the iterator helper API.')
netSnmpHostsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8072, 2, 2, 2, 1), ).setIndexNames((0, "NET-SNMP-EXAMPLES-MIB", "netSnmpHostName"))
if mibBuilder.loadTexts: netSnmpHostsEntry.setStatus('current')
if mibBuilder.loadTexts: netSnmpHostsEntry.setDescription('A host name mapped to an ip address')
netSnmpHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 2, 2, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)))
if mibBuilder.loadTexts: netSnmpHostName.setStatus('current')
if mibBuilder.loadTexts: netSnmpHostName.setDescription('A host name that exists in the /etc/hosts (unix) file.')
netSnmpHostAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 2, 2, 2, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: netSnmpHostAddressType.setStatus('current')
if mibBuilder.loadTexts: netSnmpHostAddressType.setDescription('The address type of then given host.')
netSnmpHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 2, 2, 2, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: netSnmpHostAddress.setStatus('current')
if mibBuilder.loadTexts: netSnmpHostAddress.setDescription('The address of then given host.')
netSnmpHostStorage = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 2, 2, 2, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: netSnmpHostStorage.setStatus('current')
if mibBuilder.loadTexts: netSnmpHostStorage.setDescription('The storage type for this conceptual row.')
netSnmpHostRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 2, 2, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: netSnmpHostRowStatus.setStatus('current')
if mibBuilder.loadTexts: netSnmpHostRowStatus.setDescription('The status of this conceptual row.')
netSnmpExampleHeartbeatRate = MibScalar((1, 3, 6, 1, 4, 1, 8072, 2, 3, 2, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: netSnmpExampleHeartbeatRate.setStatus('current')
if mibBuilder.loadTexts: netSnmpExampleHeartbeatRate.setDescription('A simple integer object, to act as a payload for the netSnmpExampleHeartbeatNotification. The value has no real meaning, but is nominally the interval (in seconds) between successive heartbeat notifications.')
netSnmpExampleHeartbeatName = MibScalar((1, 3, 6, 1, 4, 1, 8072, 2, 3, 2, 2), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: netSnmpExampleHeartbeatName.setStatus('current')
if mibBuilder.loadTexts: netSnmpExampleHeartbeatName.setDescription("A simple string object, to act as an optional payload for the netSnmpExampleHeartbeatNotification. This varbind is not part of the notification definition, so is optional and need not be included in the notification payload. The value has no real meaning, but the romantically inclined may take it to be the object of the sender's affection, and hence the cause of the heart beating faster.")
netSnmpExampleHeartbeatNotification = NotificationType((1, 3, 6, 1, 4, 1, 8072, 2, 3, 0, 1)).setObjects(("NET-SNMP-EXAMPLES-MIB", "netSnmpExampleHeartbeatRate"))
if mibBuilder.loadTexts: netSnmpExampleHeartbeatNotification.setStatus('current')
if mibBuilder.loadTexts: netSnmpExampleHeartbeatNotification.setDescription('An example notification, used to illustrate the definition and generation of trap and inform PDUs (including the use of both standard and additional varbinds in the notification payload). This notification will typically be sent every 30 seconds, using the code found in the example module agent/mibgroup/examples/notification.c')
netSnmpExampleNotification = MibScalar((1, 3, 6, 1, 4, 1, 8072, 2, 3, 1), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: netSnmpExampleNotification.setStatus('obsolete')
if mibBuilder.loadTexts: netSnmpExampleNotification.setDescription('This object was improperly defined for its original purpose, and should no longer be used.')
mibBuilder.exportSymbols("NET-SNMP-EXAMPLES-MIB", netSnmpExampleString=netSnmpExampleString, netSnmpIETFWGEntry=netSnmpIETFWGEntry, netSnmpExampleSleeper=netSnmpExampleSleeper, netSnmpIETFWGTable=netSnmpIETFWGTable, PYSNMP_MODULE_ID=netSnmpExamples, netSnmpHostStorage=netSnmpHostStorage, nsIETFWGChair2=nsIETFWGChair2, nsIETFWGChair1=nsIETFWGChair1, netSnmpHostRowStatus=netSnmpHostRowStatus, netSnmpExampleInteger=netSnmpExampleInteger, nsIETFWGName=nsIETFWGName, netSnmpHostsTable=netSnmpHostsTable, netSnmpExampleScalars=netSnmpExampleScalars, netSnmpExampleHeartbeatName=netSnmpExampleHeartbeatName, netSnmpHostName=netSnmpHostName, netSnmpExampleNotificationObjects=netSnmpExampleNotificationObjects, netSnmpExampleHeartbeatNotification=netSnmpExampleHeartbeatNotification, netSnmpHostsEntry=netSnmpHostsEntry, netSnmpExampleHeartbeatRate=netSnmpExampleHeartbeatRate, netSnmpExampleNotificationPrefix=netSnmpExampleNotificationPrefix, netSnmpExamples=netSnmpExamples, netSnmpExampleNotifications=netSnmpExampleNotifications, netSnmpHostAddressType=netSnmpHostAddressType, netSnmpExampleTables=netSnmpExampleTables, netSnmpExampleNotification=netSnmpExampleNotification, netSnmpHostAddress=netSnmpHostAddress)
