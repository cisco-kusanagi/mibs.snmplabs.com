#
# PySNMP MIB module CISCO-DTI-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DTI-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:39:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
dtiProtocolClientStatusFlag, dtiProtocolServerStatusFlag = mibBuilder.importSymbols("DTI-MIB", "dtiProtocolClientStatusFlag", "dtiProtocolServerStatusFlag")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, Unsigned32, ModuleIdentity, Integer32, Counter32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, iso, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "Unsigned32", "ModuleIdentity", "Integer32", "Counter32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "iso", "ObjectIdentity", "IpAddress")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ciscoDtiExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 822))
ciscoDtiExtMIB.setRevisions(('2014-08-22 00:00',))
if mibBuilder.loadTexts: ciscoDtiExtMIB.setLastUpdated('201408220000Z')
if mibBuilder.loadTexts: ciscoDtiExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoDtiExtNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 822, 0))
ciscoDtiExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 822, 1))
ciscoDtiExtConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 822, 2))
cdeServerStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 822, 0, 1)).setObjects(("DTI-MIB", "dtiProtocolServerStatusFlag"))
if mibBuilder.loadTexts: cdeServerStatusChange.setStatus('current')
cdeClientStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 822, 0, 2)).setObjects(("DTI-MIB", "dtiProtocolClientStatusFlag"))
if mibBuilder.loadTexts: cdeClientStatusChange.setStatus('current')
ciscoDtiExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 1))
cdeServerStatusChangeEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 822, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeServerStatusChangeEnable.setStatus('current')
cdeClientStatusChangeEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 822, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeClientStatusChangeEnable.setStatus('current')
ciscoDtiExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 2))
ciscoDtiExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 1, 1)).setObjects(("CISCO-DTI-EXT-MIB", "ciscoDtiExtNotifsControlGroup"), ("CISCO-DTI-EXT-MIB", "ciscoDtiExtNotifsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDtiExtCompliance = ciscoDtiExtCompliance.setStatus('current')
ciscoDtiExtNotifsControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 2, 1)).setObjects(("CISCO-DTI-EXT-MIB", "cdeServerStatusChangeEnable"), ("CISCO-DTI-EXT-MIB", "cdeClientStatusChangeEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDtiExtNotifsControlGroup = ciscoDtiExtNotifsControlGroup.setStatus('current')
ciscoDtiExtNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 822, 2, 2, 2)).setObjects(("CISCO-DTI-EXT-MIB", "cdeServerStatusChange"), ("CISCO-DTI-EXT-MIB", "cdeClientStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDtiExtNotifsGroup = ciscoDtiExtNotifsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DTI-EXT-MIB", ciscoDtiExtMIB=ciscoDtiExtMIB, ciscoDtiExtNotifsGroup=ciscoDtiExtNotifsGroup, PYSNMP_MODULE_ID=ciscoDtiExtMIB, cdeClientStatusChange=cdeClientStatusChange, ciscoDtiExtGroups=ciscoDtiExtGroups, ciscoDtiExtCompliance=ciscoDtiExtCompliance, cdeClientStatusChangeEnable=cdeClientStatusChangeEnable, cdeServerStatusChange=cdeServerStatusChange, ciscoDtiExtNotifsControlGroup=ciscoDtiExtNotifsControlGroup, ciscoDtiExtObjects=ciscoDtiExtObjects, ciscoDtiExtNotifs=ciscoDtiExtNotifs, ciscoDtiExtConform=ciscoDtiExtConform, cdeServerStatusChangeEnable=cdeServerStatusChangeEnable, ciscoDtiExtCompliances=ciscoDtiExtCompliances)
