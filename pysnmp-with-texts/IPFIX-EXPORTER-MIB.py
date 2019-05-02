#
# PySNMP MIB module IPFIX-EXPORTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPFIX-EXPORTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:55:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressType, InetAddress, InetAutonomousSystemNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress", "InetAutonomousSystemNumber")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, Counter64, TimeTicks, mib_2, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, IpAddress, Bits, MibIdentifier, NotificationType, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "TimeTicks", "mib-2", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "IpAddress", "Bits", "MibIdentifier", "NotificationType", "ObjectIdentity", "iso")
DateAndTime, RowStatus, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "RowStatus", "TruthValue", "DisplayString", "TextualConvention")
ipfixMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 999))
ipfixMIB.setRevisions(('2006-10-23 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ipfixMIB.setRevisionsDescriptions(('Initial version, published as RFC yyyy.',))
if mibBuilder.loadTexts: ipfixMIB.setLastUpdated('200610231200Z')
if mibBuilder.loadTexts: ipfixMIB.setOrganization('IETF IP Flow Information Export')
if mibBuilder.loadTexts: ipfixMIB.setContactInfo('WG charter: http://www.ietf.org/html.charters/ipfix-charter.html Mailing Lists: General Discussion: ipfix@net.doit.wisc.edu To Subscribe: majordomo@net.doit.wisc.edu In Body: subscribe ipfix Archive: http://ipfix.doit.wisc.edu/archive/ Editor: Thomas Dietz NEC Europe Ltd. Network Laboratories Kurfuersten-Anlage 36 69115 Heidelberg Germany Phone: +49 6221 4342-128 Email: dietz@netlab.nec.de')
if mibBuilder.loadTexts: ipfixMIB.setDescription('The IPFIX MIB defines managed objects for IP flow information export. These objects provide information about managed nodes supporting IP flow information export, including flow information export capabilities, configuration and statistics. They also allow to configure IP flow information export concerning the IP interface at which flow information is gathered, the flow selections methods used, and the collector to which flow information is exported. Copyright (C) The Internet Society (2006). This version of this MIB module is part of RFC yyyy; see the RFC itself for full legal notices.')
class PsampMethodAvailability(TextualConvention, Integer32):
    description = 'Used to report the availability of a selection method: available(1) - the method is supported and can be used notAvailable(2) - the method is not available'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("available", 1), ("notAvailable", 2))

ipfixExporter = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 1))
ipfixCollector = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 2))
ipfixPsampExtension = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 3))
ipfixConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 4))
ipfixExporterObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 1, 1))
ipfixReporting = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 1, 1, 1))
ipfixCollectorTable = MibTable((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1), )
if mibBuilder.loadTexts: ipfixCollectorTable.setStatus('current')
if mibBuilder.loadTexts: ipfixCollectorTable.setDescription('This table lists collectors to which reports are exported.')
ipfixCollectorEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 1), ).setIndexNames((0, "IPFIX-EXPORTER-MIB", "ipfixCollectorIndex"))
if mibBuilder.loadTexts: ipfixCollectorEntry.setStatus('current')
if mibBuilder.loadTexts: ipfixCollectorEntry.setDescription('Defines an entry in the ipfixCollectorTable.')
ipfixCollectorIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ipfixCollectorIndex.setStatus('current')
if mibBuilder.loadTexts: ipfixCollectorIndex.setDescription("The locally arbitrary, but unique identifier of a collector. The value is expected to remain constant at least from one re-initialization of the entity's network management system to the next re-initialization.")
ipfixCollectorDstIpAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipfixCollectorDstIpAddressType.setStatus('current')
if mibBuilder.loadTexts: ipfixCollectorDstIpAddressType.setDescription('The IP address type of the collector.')
ipfixCollectorDstIpAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipfixCollectorDstIpAddress.setStatus('current')
if mibBuilder.loadTexts: ipfixCollectorDstIpAddress.setDescription('The IP address of the collector.')
ipfixCollectorDstProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256)).clone(132)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipfixCollectorDstProtocol.setStatus('current')
if mibBuilder.loadTexts: ipfixCollectorDstProtocol.setDescription('The transport protocol used for exporting sampled packets to the collector. The recommended protocols are TCP (6), UDP (17) and SCTP (132). The default is SCTP.')
ipfixCollectorDstPort = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipfixCollectorDstPort.setStatus('current')
if mibBuilder.loadTexts: ipfixCollectorDstPort.setDescription('The port number of the collector.')
ipfixCollectorReportsSent = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixCollectorReportsSent.setStatus('current')
if mibBuilder.loadTexts: ipfixCollectorReportsSent.setDescription('The number of reports sent to the collector.')
ipfixCollectorGroupTable = MibTable((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 2), )
if mibBuilder.loadTexts: ipfixCollectorGroupTable.setStatus('current')
if mibBuilder.loadTexts: ipfixCollectorGroupTable.setDescription('This table lists groups of collectors to which flow records packets are exported. If flow records are exported to only one collector the group consists of exactly one collector.')
ipfixCollectorGroupEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 2, 1), ).setIndexNames((0, "IPFIX-EXPORTER-MIB", "ipfixCollectorGroupIndex"), (0, "IPFIX-EXPORTER-MIB", "ipfixCollectorIndex"))
if mibBuilder.loadTexts: ipfixCollectorGroupEntry.setStatus('current')
if mibBuilder.loadTexts: ipfixCollectorGroupEntry.setDescription('Defines an entry in the ipfixCollectorGroupTable.')
ipfixCollectorGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ipfixCollectorGroupIndex.setStatus('current')
if mibBuilder.loadTexts: ipfixCollectorGroupIndex.setDescription("The locally arbitrary, but unique identifier of a collector group. The value is expected to remain constant at least from one re-initialization of the entity's network management system to the next re-initialization.")
ipfixTemplateTable = MibTable((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 3), )
if mibBuilder.loadTexts: ipfixTemplateTable.setStatus('current')
if mibBuilder.loadTexts: ipfixTemplateTable.setDescription('This table lists templates used by the exporter.')
ipfixTemplateEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 3, 1), ).setIndexNames((0, "IPFIX-EXPORTER-MIB", "ipfixObservationDomainId"), (0, "IPFIX-EXPORTER-MIB", "ipfixTemplateId"), (0, "IPFIX-EXPORTER-MIB", "ipfixTemplateIndex"))
if mibBuilder.loadTexts: ipfixTemplateEntry.setStatus('current')
if mibBuilder.loadTexts: ipfixTemplateEntry.setDescription('Defines an entry in the ipfixTemplateTable.')
ipfixTemplateId = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ipfixTemplateId.setReference('draft-ietf-ipfix-sample-tech-04.txt, Section 5.1')
if mibBuilder.loadTexts: ipfixTemplateId.setStatus('current')
if mibBuilder.loadTexts: ipfixTemplateId.setDescription('The unique identifier for the template.')
ipfixTemplateIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ipfixTemplateIndex.setStatus('current')
if mibBuilder.loadTexts: ipfixTemplateIndex.setDescription("The locally arbitrary, but unique identifier of a field Id in the template identified by ipfixTemplateId. The value is expected to remain constant at least from one re-initialization of the entity's network management system to the next re-initialization.")
ipfixTemplateFieldId = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixTemplateFieldId.setReference('draft-ietf-ipfix-sample-tech-04.txt, IPFIX/PSAMP INFO MODEL')
if mibBuilder.loadTexts: ipfixTemplateFieldId.setStatus('current')
if mibBuilder.loadTexts: ipfixTemplateFieldId.setDescription('The Field Id at position ipfixTemplateIndex in the template ipfixTemplateId. This implicitly gives the data type and state values that are exported.')
ipfixTemplateFieldLength = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixTemplateFieldLength.setStatus('current')
if mibBuilder.loadTexts: ipfixTemplateFieldLength.setDescription('The Length of the Field. Used to indicate if reduced encoding or variable length field is used.')
ipfixInstances = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 1, 1, 2))
ipfixObservationDomainTable = MibTable((1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 1), )
if mibBuilder.loadTexts: ipfixObservationDomainTable.setStatus('current')
if mibBuilder.loadTexts: ipfixObservationDomainTable.setDescription('This table lists the Observation Domains used at the managed node.')
ipfixObservationDomainEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 1, 1), ).setIndexNames((0, "IPFIX-EXPORTER-MIB", "ipfixObservationDomainId"))
if mibBuilder.loadTexts: ipfixObservationDomainEntry.setStatus('current')
if mibBuilder.loadTexts: ipfixObservationDomainEntry.setDescription('Defines an entry in the ipfixObservationDomainTable.')
ipfixObservationDomainId = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ipfixObservationDomainId.setStatus('current')
if mibBuilder.loadTexts: ipfixObservationDomainId.setDescription("The locally arbitrary, but unique identifier of an Observation Domain. The value is expected to remain constant at least from one re-initialization of the entity's network management system to the next re-initialization.")
ipfixInstanceObservationPoint = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipfixInstanceObservationPoint.setStatus('current')
if mibBuilder.loadTexts: ipfixInstanceObservationPoint.setDescription('The point where the packet is observed. If it is e.g, an interface it points to the mib-II object of the interface.')
ipfixInstanceStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 1, 1, 3), DateAndTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipfixInstanceStartTime.setStatus('current')
if mibBuilder.loadTexts: ipfixInstanceStartTime.setDescription('The date and time when exporting for this parameter set should start.')
ipfixInstanceStopTime = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 1, 1, 4), DateAndTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipfixInstanceStopTime.setStatus('current')
if mibBuilder.loadTexts: ipfixInstanceStopTime.setDescription('The date and time when exporting for this parameter set should stop.')
ipfixInstanceTable = MibTable((1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 2), )
if mibBuilder.loadTexts: ipfixInstanceTable.setStatus('current')
if mibBuilder.loadTexts: ipfixInstanceTable.setDescription('This table lists active instances of packet sampling at the managed node.')
ipfixInstanceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 2, 1), ).setIndexNames((0, "IPFIX-EXPORTER-MIB", "ipfixInstanceIndex"), (0, "IPFIX-EXPORTER-MIB", "ipfixObservationDomainId"))
if mibBuilder.loadTexts: ipfixInstanceEntry.setStatus('current')
if mibBuilder.loadTexts: ipfixInstanceEntry.setDescription('Defines an entry in the ipfixInstanceTable.')
ipfixInstanceIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ipfixInstanceIndex.setStatus('current')
if mibBuilder.loadTexts: ipfixInstanceIndex.setDescription("The locally arbitrary, but unique identifier of an instance. The value is expected to remain constant at least from one re-initialization of the entity's network management system to the next re-initialization.")
ipfixInstanceTemplateId = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipfixInstanceTemplateId.setStatus('current')
if mibBuilder.loadTexts: ipfixInstanceTemplateId.setDescription('The Id of a template in the template table. This implies the knowledge about the method chain from the method chain table. Furthermore it links the instance, method chain (selector) and template together. The identified template is applied to the stream of filtered/sampled packets observed after applying the method chain at the observation point.')
ipfixInstanceCollectorGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 2, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipfixInstanceCollectorGroupIndex.setStatus('current')
if mibBuilder.loadTexts: ipfixInstanceCollectorGroupIndex.setDescription('The index of the collector group to which packet reports are sent.')
ipfixInstancePacketsObserved = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixInstancePacketsObserved.setStatus('current')
if mibBuilder.loadTexts: ipfixInstancePacketsObserved.setDescription('The number of packets observed at the observation point.')
ipfixInstancePacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixInstancePacketsDropped.setStatus('current')
if mibBuilder.loadTexts: ipfixInstancePacketsDropped.setDescription('The number of packets dropped while filtering/sampling packets.')
ipfixInstanceProcessId = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixInstanceProcessId.setStatus('current')
if mibBuilder.loadTexts: ipfixInstanceProcessId.setDescription('The process id of the metering process used by this instance.')
ipfixInstanceReportingProcessId = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixInstanceReportingProcessId.setStatus('current')
if mibBuilder.loadTexts: ipfixInstanceReportingProcessId.setDescription('The process id of the reporting process used by this instance.')
ipfixInstanceReportsSent = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixInstanceReportsSent.setStatus('current')
if mibBuilder.loadTexts: ipfixInstanceReportsSent.setDescription('The number of reports on sampled packets sent to the collector.')
ipfixMethodChainTable = MibTable((1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 4), )
if mibBuilder.loadTexts: ipfixMethodChainTable.setStatus('current')
if mibBuilder.loadTexts: ipfixMethodChainTable.setDescription('This table contains method chains lists and connects them to the instances where they are applied to different observation points. The filtered/sampled packets are then exported.')
ipfixMethodChainEntry = MibTableRow((1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 4, 1), ).setIndexNames((0, "IPFIX-EXPORTER-MIB", "ipfixInstanceIndex"), (0, "IPFIX-EXPORTER-MIB", "ipfixMethodChainIndex"))
if mibBuilder.loadTexts: ipfixMethodChainEntry.setStatus('current')
if mibBuilder.loadTexts: ipfixMethodChainEntry.setDescription('Defines an entry in the ipfixMethodChainTable.')
ipfixMethodChainIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ipfixMethodChainIndex.setStatus('current')
if mibBuilder.loadTexts: ipfixMethodChainIndex.setDescription("The locally arbitrary, but unique identifier of a template. The value is expected to remain constant at least from one re-initialization of the entity's network management system to the next re-initialization.")
ipfixMethodChainMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 4, 1, 3), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipfixMethodChainMethod.setStatus('current')
if mibBuilder.loadTexts: ipfixMethodChainMethod.setDescription('The method used for the template at a certain position in the method chain.')
ipfixMethodChainPacketsObserved = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixMethodChainPacketsObserved.setStatus('current')
if mibBuilder.loadTexts: ipfixMethodChainPacketsObserved.setDescription('The number of packets observed at the method entry point.')
ipfixMethodChainPacketsDropped = MibTableColumn((1, 3, 6, 1, 2, 1, 999, 1, 1, 2, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipfixMethodChainPacketsDropped.setStatus('current')
if mibBuilder.loadTexts: ipfixMethodChainPacketsDropped.setDescription('The number of packets dropped while selecting packets.')
ipfixCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 4, 1))
ipfixGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 999, 4, 2))
ipfixCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 999, 4, 1, 1)).setObjects(("IPFIX-EXPORTER-MIB", "ipfixGroupMetering"), ("IPFIX-EXPORTER-MIB", "ipfixGroupReporting"), ("IPFIX-EXPORTER-MIB", "ipfixGroupStatistics"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipfixCompliance = ipfixCompliance.setStatus('current')
if mibBuilder.loadTexts: ipfixCompliance.setDescription('An implementation that complies to this module must implement the objects defined in the mandatory groups ipfixGroupMetering and ipfixGroupReporting. The implementation of all other objects depends on the implementation of the corresponding functionality in the equipment.')
ipfixGroupMetering = ObjectGroup((1, 3, 6, 1, 2, 1, 999, 4, 2, 1)).setObjects(("IPFIX-EXPORTER-MIB", "ipfixTemplateFieldId"), ("IPFIX-EXPORTER-MIB", "ipfixTemplateFieldLength"), ("IPFIX-EXPORTER-MIB", "ipfixMethodChainMethod"), ("IPFIX-EXPORTER-MIB", "ipfixInstanceObservationPoint"), ("IPFIX-EXPORTER-MIB", "ipfixInstanceStartTime"), ("IPFIX-EXPORTER-MIB", "ipfixInstanceStopTime"), ("IPFIX-EXPORTER-MIB", "ipfixInstanceTemplateId"), ("IPFIX-EXPORTER-MIB", "ipfixInstanceCollectorGroupIndex"), ("IPFIX-EXPORTER-MIB", "ipfixInstanceProcessId"), ("IPFIX-EXPORTER-MIB", "ipfixInstanceReportingProcessId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipfixGroupMetering = ipfixGroupMetering.setStatus('current')
if mibBuilder.loadTexts: ipfixGroupMetering.setDescription('All objects that are basic for the metering process. It contains a basic metering function (ipfixSelectAll), The template definitions needed for the export of data, the method chain that fixes the metering functions applied to the observation point and several parameters concering the export process and the collectors.')
ipfixGroupReporting = ObjectGroup((1, 3, 6, 1, 2, 1, 999, 4, 2, 2)).setObjects(("IPFIX-EXPORTER-MIB", "ipfixCollectorDstIpAddressType"), ("IPFIX-EXPORTER-MIB", "ipfixCollectorDstIpAddress"), ("IPFIX-EXPORTER-MIB", "ipfixCollectorDstProtocol"), ("IPFIX-EXPORTER-MIB", "ipfixCollectorDstPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipfixGroupReporting = ipfixGroupReporting.setStatus('current')
if mibBuilder.loadTexts: ipfixGroupReporting.setDescription('These objects define the collectors i.e., the destinations of the exporting process.')
ipfixGroupStatistics = ObjectGroup((1, 3, 6, 1, 2, 1, 999, 4, 2, 3)).setObjects(("IPFIX-EXPORTER-MIB", "ipfixCollectorReportsSent"), ("IPFIX-EXPORTER-MIB", "ipfixMethodChainPacketsObserved"), ("IPFIX-EXPORTER-MIB", "ipfixMethodChainPacketsDropped"), ("IPFIX-EXPORTER-MIB", "ipfixInstancePacketsObserved"), ("IPFIX-EXPORTER-MIB", "ipfixInstanceReportsSent"), ("IPFIX-EXPORTER-MIB", "ipfixInstancePacketsDropped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipfixGroupStatistics = ipfixGroupStatistics.setStatus('current')
if mibBuilder.loadTexts: ipfixGroupStatistics.setDescription('These objects contain statistical values gathered at different points in the metering process.')
mibBuilder.exportSymbols("IPFIX-EXPORTER-MIB", ipfixMethodChainPacketsDropped=ipfixMethodChainPacketsDropped, ipfixTemplateIndex=ipfixTemplateIndex, ipfixPsampExtension=ipfixPsampExtension, ipfixMethodChainIndex=ipfixMethodChainIndex, ipfixInstanceIndex=ipfixInstanceIndex, ipfixCompliance=ipfixCompliance, ipfixCollectorGroupTable=ipfixCollectorGroupTable, ipfixCollectorEntry=ipfixCollectorEntry, ipfixObservationDomainTable=ipfixObservationDomainTable, ipfixObservationDomainId=ipfixObservationDomainId, ipfixCollectorDstIpAddress=ipfixCollectorDstIpAddress, ipfixInstanceEntry=ipfixInstanceEntry, ipfixInstancePacketsDropped=ipfixInstancePacketsDropped, ipfixExporter=ipfixExporter, PYSNMP_MODULE_ID=ipfixMIB, ipfixConformance=ipfixConformance, PsampMethodAvailability=PsampMethodAvailability, ipfixGroups=ipfixGroups, ipfixInstanceStopTime=ipfixInstanceStopTime, ipfixInstanceProcessId=ipfixInstanceProcessId, ipfixInstanceReportingProcessId=ipfixInstanceReportingProcessId, ipfixExporterObjects=ipfixExporterObjects, ipfixInstanceObservationPoint=ipfixInstanceObservationPoint, ipfixTemplateTable=ipfixTemplateTable, ipfixTemplateEntry=ipfixTemplateEntry, ipfixGroupMetering=ipfixGroupMetering, ipfixReporting=ipfixReporting, ipfixCollectorIndex=ipfixCollectorIndex, ipfixInstanceCollectorGroupIndex=ipfixInstanceCollectorGroupIndex, ipfixCompliances=ipfixCompliances, ipfixCollector=ipfixCollector, ipfixTemplateId=ipfixTemplateId, ipfixCollectorDstIpAddressType=ipfixCollectorDstIpAddressType, ipfixCollectorGroupIndex=ipfixCollectorGroupIndex, ipfixInstanceTemplateId=ipfixInstanceTemplateId, ipfixInstanceTable=ipfixInstanceTable, ipfixInstanceReportsSent=ipfixInstanceReportsSent, ipfixMethodChainMethod=ipfixMethodChainMethod, ipfixCollectorDstProtocol=ipfixCollectorDstProtocol, ipfixCollectorTable=ipfixCollectorTable, ipfixGroupStatistics=ipfixGroupStatistics, ipfixObservationDomainEntry=ipfixObservationDomainEntry, ipfixCollectorGroupEntry=ipfixCollectorGroupEntry, ipfixInstanceStartTime=ipfixInstanceStartTime, ipfixInstancePacketsObserved=ipfixInstancePacketsObserved, ipfixInstances=ipfixInstances, ipfixMethodChainEntry=ipfixMethodChainEntry, ipfixMIB=ipfixMIB, ipfixGroupReporting=ipfixGroupReporting, ipfixMethodChainPacketsObserved=ipfixMethodChainPacketsObserved, ipfixCollectorReportsSent=ipfixCollectorReportsSent, ipfixTemplateFieldLength=ipfixTemplateFieldLength, ipfixCollectorDstPort=ipfixCollectorDstPort, ipfixMethodChainTable=ipfixMethodChainTable, ipfixTemplateFieldId=ipfixTemplateFieldId)
