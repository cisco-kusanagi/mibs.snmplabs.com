#
# PySNMP MIB module CISCO-VQE-TOOLS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VQE-TOOLS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:03:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, ModuleIdentity, TimeTicks, ObjectIdentity, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, Unsigned32, NotificationType, iso, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "Unsigned32", "NotificationType", "iso", "IpAddress", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVqeToolsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 969))
ciscoVqeToolsMIB.setRevisions(('2009-12-18 13:41',))
if mibBuilder.loadTexts: ciscoVqeToolsMIB.setLastUpdated('200912181341Z')
if mibBuilder.loadTexts: ciscoVqeToolsMIB.setOrganization('Cisco Systems, Inc.')
ciscoVqeToolsMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 0))
ciscoVqeToolsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 1))
ciscoVqeToolsMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 2))
cvqtVcdsInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1))
cvqtNumberOfSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 1), Gauge32()).setUnits('RTSP connections').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvqtNumberOfSessions.setStatus('current')
cvqtTotalReceivedRequests = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 2), Counter64()).setUnits('RTSP requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvqtTotalReceivedRequests.setStatus('current')
cvqtTotalSentResponses = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 3), Counter64()).setUnits('RTSP responses').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvqtTotalSentResponses.setStatus('current')
cvqtRequestRate = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 969, 1, 1, 4), Gauge32()).setUnits('requests per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cvqtRequestRate.setStatus('current')
cvqtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 1))
cvqtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 2))
cvqtMIBReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 1, 1)).setObjects(("CISCO-VQE-TOOLS-MIB", "ciscoVqeToolsVcdsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvqtMIBReadOnlyCompliance = cvqtMIBReadOnlyCompliance.setStatus('current')
ciscoVqeToolsVcdsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 969, 2, 2, 1)).setObjects(("CISCO-VQE-TOOLS-MIB", "cvqtNumberOfSessions"), ("CISCO-VQE-TOOLS-MIB", "cvqtTotalReceivedRequests"), ("CISCO-VQE-TOOLS-MIB", "cvqtTotalSentResponses"), ("CISCO-VQE-TOOLS-MIB", "cvqtRequestRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVqeToolsVcdsGroup = ciscoVqeToolsVcdsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VQE-TOOLS-MIB", cvqtMIBReadOnlyCompliance=cvqtMIBReadOnlyCompliance, cvqtTotalSentResponses=cvqtTotalSentResponses, cvqtNumberOfSessions=cvqtNumberOfSessions, ciscoVqeToolsMIBObjects=ciscoVqeToolsMIBObjects, cvqtTotalReceivedRequests=cvqtTotalReceivedRequests, ciscoVqeToolsMIB=ciscoVqeToolsMIB, ciscoVqeToolsMIBNotifs=ciscoVqeToolsMIBNotifs, ciscoVqeToolsVcdsGroup=ciscoVqeToolsVcdsGroup, cvqtMIBGroups=cvqtMIBGroups, cvqtRequestRate=cvqtRequestRate, cvqtMIBCompliances=cvqtMIBCompliances, cvqtVcdsInfo=cvqtVcdsInfo, ciscoVqeToolsMIBConform=ciscoVqeToolsMIBConform, PYSNMP_MODULE_ID=ciscoVqeToolsMIB)
