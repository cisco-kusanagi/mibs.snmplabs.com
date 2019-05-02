#
# PySNMP MIB module SUN-CLUSTER-EVENTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SUN-CLUSTER-EVENTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:12:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, TimeTicks, Unsigned32, NotificationType, Counter64, MibIdentifier, ModuleIdentity, Gauge32, iso, IpAddress, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "TimeTicks", "Unsigned32", "NotificationType", "Counter64", "MibIdentifier", "ModuleIdentity", "Gauge32", "iso", "IpAddress", "ObjectIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sunClusterEventsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 42, 2, 80, 2))
sunClusterEventsMIB.setRevisions(('1902-11-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: sunClusterEventsMIB.setRevisionsDescriptions(('Draft.',))
if mibBuilder.loadTexts: sunClusterEventsMIB.setLastUpdated('0211300000Z')
if mibBuilder.loadTexts: sunClusterEventsMIB.setOrganization('Sun Microsystems')
if mibBuilder.loadTexts: sunClusterEventsMIB.setContactInfo('Sun Microsystems')
if mibBuilder.loadTexts: sunClusterEventsMIB.setDescription('Oracle Solaris Cluster Event MIB monitors the event framework')
sun = MibIdentifier((1, 3, 6, 1, 4, 1, 42))
prod = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2))
suncluster = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 80))
scEventsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1))
scEventsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 2))
class ScEventTableCount(TextualConvention, Integer32):
    description = 'Maximum number of event instances maintained in this MIB. When escEventsTable has this many entries and a new entry is added, the earliest entry will be retired'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(20, 32767)

class ScEventIndex(TextualConvention, Integer32):
    description = 'An index into the tables to refer to a specific event instance'
    status = 'current'

class ScClusterId(DisplayString):
    description = 'The unique cluster ID of the cluster sending this event'
    status = 'current'

class ScClusterName(DisplayString):
    description = 'The name of the cluster sending this event'
    status = 'current'

class ScNodeName(DisplayString):
    description = 'The name of the cluster node sending this event'
    status = 'current'

class ScEventVersion(TextualConvention, Integer32):
    description = 'The version number of this event'
    status = 'current'

class ScEventClassName(DisplayString):
    description = 'Event Class Name, currently always the string EC_Cluster'
    status = 'current'

class ScEventSubclassName(DisplayString):
    description = 'Event Subclass Name could be : ESC_cluster_generic_event, ESC_cluster_config_change, ESC_cluster_state_change, ESC_cluster_node_config_change, ESC_cluster_node_state_change, ESC_cluster_cmm_reconfig, ESC_cluster_ucmm_reconfig, ESC_cluster_ucmm_reconfig_substep, ESC_cluster_quorum_config_change, ESC_cluster_quorum_state_change, ESC_cluster_membership,ESC_cluster_rg_state, ESC_cluster_rg_primaries_changing, ESC_cluster_rg_remaining_offlin, ESC_cluster_rg_giveover_deferred, ESC_cluster_rg_node_rebooted, ESC_cluster_rg_config_change, ESC_cluster_r_state ESC_cluster_r_method_completed, ESC_cluster_r_config_chang, ESC_cluster_fm_r_status_change, ESC_cluster_fm_r_restarting, ESC_cluster_scha_api_invalid, ESC_cluster_pmf_proc_restart, ESC_cluster_pmf_proc_not_restarted, ESC_cluster_tp_path_config_change, ESC_cluster_tp_path_config_change, ESC_cluster_tp_path_state_change, ESC_cluster_tp_if_state_change, ESC_cluster_ipmp_group_state, ESC_cluster_ipmp_group_change, ESC_cluster_ipmp_group_member_change, ESC_cluster_ipmp_if_change '
    status = 'current'

class ScEventSeverity(TextualConvention, Integer32):
    description = 'Event severity : CL_EVENT_SEV_INFO = 0 CL_EVENT_SEV_WARNING = 1 CL_EVENT_SEV_ERROR = 2 CL_EVENT_SEV_CRITICAL = 3 CL_EVENT_SEV_FATAL = 4 '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("clEventSevInfo", 0), ("clEventSevWarning", 1), ("clEventSevError", 2), ("clEventSevCritical", 3), ("clEventSevFatal", 4))

class ScEventInitiator(TextualConvention, Integer32):
    description = 'Event severity : CL_EVENT_INIT_UNKNOWN = 0, CL_EVENT_INIT_SYSTEM = 1, CL_EVENT_INIT_OPERATOR = 2, CL_EVENT_INIT_AGENT = 3, '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("clEventInitUnknown", 0), ("clEventInitSystem", 1), ("clEventInitOperator", 2), ("clEventInitAgent", 3))

class ScEventPublisher(DisplayString):
    description = 'Publisher name could be : rgm pmf cmm net dcs dpm tp ucmm '
    status = 'current'

class ScEventPid(TextualConvention, Counter64):
    description = 'The process PID issuing the event'
    status = 'current'

class ScTimeStamp(TextualConvention, Counter64):
    description = 'The difference, measured in milliseconds, between the current time and midnight, January 1, 1970 UTC.'
    status = 'current'

class ScEventData(DisplayString):
    description = 'More detail data of the event, concate attribute name/value'
    status = 'current'

class ScEventAttributeName(DisplayString):
    description = 'Name of the attributes could be rt_name, rg_name, r_name, quorum_name, method_name tp_path_name, tp_if_name, affinity_rg_name, node_list state_list, from_node_list, to_node_list, old_state new_state, old_status, new_status, status_msg step_name, substep_name, start_time, duration, method_duration method_path, scha_api_optag, scha_api_func, pmf_name_tag, pmf_cmd_path total_attempts, attempt_number, cmd_path, retry_number retry_count, vote_count, desired_primaries '
    status = 'current'

class ScEventAttributeValue(DisplayString):
    description = 'All attributes value are DisplayString '
    status = 'current'

escEventTableCount = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 1), ScEventTableCount()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: escEventTableCount.setStatus('current')
if mibBuilder.loadTexts: escEventTableCount.setDescription('Maximum number of event instances maintained in this MIB. When escEventsTable has this many entries and a new entry is added, the earliest entry will be retired')
escEventsTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2), )
if mibBuilder.loadTexts: escEventsTable.setStatus('current')
if mibBuilder.loadTexts: escEventsTable.setDescription('The table contains one entry per CMM Events')
escEventsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1), ).setIndexNames((0, "SUN-CLUSTER-EVENTS-MIB", "eventIndex"))
if mibBuilder.loadTexts: escEventsEntry.setStatus('current')
if mibBuilder.loadTexts: escEventsEntry.setDescription(' The entry describes an event')
eventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 1), ScEventIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventIndex.setStatus('current')
if mibBuilder.loadTexts: eventIndex.setDescription('An index to refer to a cluster event. The index numbers increase monotonically as events are added to the MIB, and the oldest events are deleted from the MIB. If the MIB is restarted, the index number restarts from 1. Different instances of this MIB may have different index numbers for the same event instance')
eventClusterId = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 2), ScClusterId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventClusterId.setStatus('current')
if mibBuilder.loadTexts: eventClusterId.setDescription('The unique cluster ID of the cluster sending this event')
eventClusterName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 3), ScClusterName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventClusterName.setStatus('current')
if mibBuilder.loadTexts: eventClusterName.setDescription('The name of the cluster sending this event')
eventNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 4), ScNodeName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventNodeName.setStatus('current')
if mibBuilder.loadTexts: eventNodeName.setDescription('The name of the cluster node sending this event')
eventVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 5), ScEventVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventVersion.setStatus('current')
if mibBuilder.loadTexts: eventVersion.setDescription('The version number of this event')
eventClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 6), ScEventClassName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventClassName.setStatus('current')
if mibBuilder.loadTexts: eventClassName.setDescription('The name of the event class')
eventSubclassName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 7), ScEventSubclassName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventSubclassName.setStatus('current')
if mibBuilder.loadTexts: eventSubclassName.setDescription('The name of the event subclass')
eventSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 8), ScEventSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventSeverity.setStatus('current')
if mibBuilder.loadTexts: eventSeverity.setDescription('The severity of this event')
eventInitiator = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 9), ScEventInitiator()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventInitiator.setStatus('current')
if mibBuilder.loadTexts: eventInitiator.setDescription('The initiator of this event')
eventPublisher = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 10), ScEventPublisher()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventPublisher.setStatus('current')
if mibBuilder.loadTexts: eventPublisher.setDescription('the event publisher')
eventSeqNo = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventSeqNo.setStatus('current')
if mibBuilder.loadTexts: eventSeqNo.setDescription('the subclass-unique sequence number for this event')
eventPid = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 12), ScEventPid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventPid.setStatus('current')
if mibBuilder.loadTexts: eventPid.setDescription('the process ID of the event issuer')
eventTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 13), ScTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventTimeStamp.setStatus('current')
if mibBuilder.loadTexts: eventTimeStamp.setDescription('the difference, measured in milliseconds, between the current time and midnight, January 1, 1970 UTC')
eventData = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 14), ScEventData()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventData.setStatus('current')
if mibBuilder.loadTexts: eventData.setDescription('the detail data of the event')
escEventsAttributesTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 3), )
if mibBuilder.loadTexts: escEventsAttributesTable.setStatus('current')
if mibBuilder.loadTexts: escEventsAttributesTable.setDescription('A table containing additional attributes specific to a given event subclass. By keying in on the eventIndex and the name of the attribute, its value may be found. ')
escEventsAttributesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 3, 1), ).setIndexNames((0, "SUN-CLUSTER-EVENTS-MIB", "eventIndex"), (0, "SUN-CLUSTER-EVENTS-MIB", "attributeName"))
if mibBuilder.loadTexts: escEventsAttributesEntry.setStatus('current')
if mibBuilder.loadTexts: escEventsAttributesEntry.setDescription('Each entry corresponds to an associated MBean. The index of the entry is composed of the eventSubclassName. ')
attributeName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 3, 1, 1), ScEventAttributeName())
if mibBuilder.loadTexts: attributeName.setStatus('current')
if mibBuilder.loadTexts: attributeName.setDescription('Name of this attribute, used as key in table')
attributeValue = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 3, 1, 2), ScEventAttributeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attributeValue.setStatus('current')
if mibBuilder.loadTexts: attributeValue.setDescription('String value of this attribute ')
escNewEvents = NotificationType((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 2, 1)).setObjects(("SUN-CLUSTER-EVENTS-MIB", "eventIndex"), ("SUN-CLUSTER-EVENTS-MIB", "eventClusterId"), ("SUN-CLUSTER-EVENTS-MIB", "eventClusterName"), ("SUN-CLUSTER-EVENTS-MIB", "eventNodeName"), ("SUN-CLUSTER-EVENTS-MIB", "eventVersion"), ("SUN-CLUSTER-EVENTS-MIB", "eventClassName"), ("SUN-CLUSTER-EVENTS-MIB", "eventSubclassName"), ("SUN-CLUSTER-EVENTS-MIB", "eventSeverity"), ("SUN-CLUSTER-EVENTS-MIB", "eventInitiator"), ("SUN-CLUSTER-EVENTS-MIB", "eventPublisher"), ("SUN-CLUSTER-EVENTS-MIB", "eventSeqNo"), ("SUN-CLUSTER-EVENTS-MIB", "eventPid"), ("SUN-CLUSTER-EVENTS-MIB", "eventTimeStamp"), ("SUN-CLUSTER-EVENTS-MIB", "eventData"))
if mibBuilder.loadTexts: escNewEvents.setStatus('current')
if mibBuilder.loadTexts: escNewEvents.setDescription('This notification is sent when a new Event is received from the Event framework and the corresponding entry is created/modified. ')
mibBuilder.exportSymbols("SUN-CLUSTER-EVENTS-MIB", eventSeqNo=eventSeqNo, attributeValue=attributeValue, ScClusterId=ScClusterId, scEventsMIBObjects=scEventsMIBObjects, suncluster=suncluster, eventIndex=eventIndex, ScEventSubclassName=ScEventSubclassName, ScEventSeverity=ScEventSeverity, ScTimeStamp=ScTimeStamp, ScEventAttributeValue=ScEventAttributeValue, ScEventAttributeName=ScEventAttributeName, eventData=eventData, escEventsEntry=escEventsEntry, prod=prod, eventClusterId=eventClusterId, escNewEvents=escNewEvents, ScNodeName=ScNodeName, eventPublisher=eventPublisher, ScEventClassName=ScEventClassName, escEventTableCount=escEventTableCount, ScEventTableCount=ScEventTableCount, eventClassName=eventClassName, ScEventVersion=ScEventVersion, eventSubclassName=eventSubclassName, eventNodeName=eventNodeName, escEventsTable=escEventsTable, ScEventIndex=ScEventIndex, eventInitiator=eventInitiator, escEventsAttributesTable=escEventsAttributesTable, ScEventInitiator=ScEventInitiator, sun=sun, escEventsAttributesEntry=escEventsAttributesEntry, attributeName=attributeName, ScClusterName=ScClusterName, scEventsMIBNotifications=scEventsMIBNotifications, ScEventPublisher=ScEventPublisher, eventSeverity=eventSeverity, PYSNMP_MODULE_ID=sunClusterEventsMIB, eventPid=eventPid, eventVersion=eventVersion, eventTimeStamp=eventTimeStamp, eventClusterName=eventClusterName, ScEventData=ScEventData, ScEventPid=ScEventPid, sunClusterEventsMIB=sunClusterEventsMIB)
