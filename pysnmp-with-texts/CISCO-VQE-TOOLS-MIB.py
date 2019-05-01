#
# PySNMP MIB module CISCO-VQE-TOOLS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VQE-TOOLS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:19:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, NotificationType, iso, Unsigned32, ModuleIdentity, TimeTicks, MibIdentifier, Counter64, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "NotificationType", "iso", "Unsigned32", "ModuleIdentity", "TimeTicks", "MibIdentifier", "Counter64", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVqeToolsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 969))
ciscoVqeToolsMIB.setRevisions(('2009-12-18 13:41',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVqeToolsMIB.setRevisionsDescriptions(('Latest version of the MIB',))
if mibBuilder.loadTexts: ciscoVqeToolsMIB.setLastUpdated('200912181341Z')
if mibBuilder.loadTexts: ciscoVqeToolsMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVqeToolsMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: bxb-iptv-team@cisco.com')
if mibBuilder.loadTexts: ciscoVqeToolsMIB.setDescription('This MIB module defines a set of objects for monitoring the VQE Client Channel Configuration Delivery Server (VCDS) operational status: number of open connections, Real Time Streaming Protocol (RTSP) reqests received and responses sent from the VCDS. Visual Quality Experience Tools Server(VQE-Tools) is responsible for the creation, maintenance, and distribution of the channel information containing channel-lineup data.')
ciscoVqeToolsMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 0))
ciscoVqeToolsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 1))
ciscoVqeToolsMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 2))
cvqtVcdsInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1))
cvqtNumberOfSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 1), Gauge32()).setUnits('RTSP connections').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvqtNumberOfSessions.setStatus('current')
if mibBuilder.loadTexts: cvqtNumberOfSessions.setDescription('This object indicates the number of open RTSP connections between VCDS and RTSP clients.')
cvqtTotalReceivedRequests = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 2), Counter64()).setUnits('RTSP requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvqtTotalReceivedRequests.setStatus('current')
if mibBuilder.loadTexts: cvqtTotalReceivedRequests.setDescription('This object indicates the number of RTSP requests received at VCDS.')
cvqtTotalSentResponses = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 3), Counter64()).setUnits('RTSP responses').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvqtTotalSentResponses.setStatus('current')
if mibBuilder.loadTexts: cvqtTotalSentResponses.setDescription('This object indicates the number of RTSP responses sent from VCDS.')
cvqtRequestRate = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 4), Gauge32()).setUnits('requests per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvqtRequestRate.setStatus('current')
if mibBuilder.loadTexts: cvqtRequestRate.setDescription('This object indicates the number of RTSP requests received at VCDS per second.')
cvqtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 1))
cvqtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 2))
cvqtMIBReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 1, 1)).setObjects(("CISCO-VQE-TOOLS-MIB", "ciscoVqeToolsVcdsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvqtMIBReadOnlyCompliance = cvqtMIBReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: cvqtMIBReadOnlyCompliance.setDescription('The compliance statement for entities which implement this MIB.')
ciscoVqeToolsVcdsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 2, 1)).setObjects(("CISCO-VQE-TOOLS-MIB", "cvqtNumberOfSessions"), ("CISCO-VQE-TOOLS-MIB", "cvqtTotalReceivedRequests"), ("CISCO-VQE-TOOLS-MIB", "cvqtTotalSentResponses"), ("CISCO-VQE-TOOLS-MIB", "cvqtRequestRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVqeToolsVcdsGroup = ciscoVqeToolsVcdsGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoVqeToolsVcdsGroup.setDescription('A collection of objects providing the VCDS stats information.')
mibBuilder.exportSymbols("CISCO-VQE-TOOLS-MIB", ciscoVqeToolsMIBConform=ciscoVqeToolsMIBConform, cvqtMIBGroups=cvqtMIBGroups, cvqtMIBReadOnlyCompliance=cvqtMIBReadOnlyCompliance, ciscoVqeToolsMIBObjects=ciscoVqeToolsMIBObjects, cvqtMIBCompliances=cvqtMIBCompliances, ciscoVqeToolsMIB=ciscoVqeToolsMIB, PYSNMP_MODULE_ID=ciscoVqeToolsMIB, ciscoVqeToolsMIBNotifs=ciscoVqeToolsMIBNotifs, cvqtTotalReceivedRequests=cvqtTotalReceivedRequests, cvqtNumberOfSessions=cvqtNumberOfSessions, cvqtRequestRate=cvqtRequestRate, cvqtTotalSentResponses=cvqtTotalSentResponses, cvqtVcdsInfo=cvqtVcdsInfo, ciscoVqeToolsVcdsGroup=ciscoVqeToolsVcdsGroup)
