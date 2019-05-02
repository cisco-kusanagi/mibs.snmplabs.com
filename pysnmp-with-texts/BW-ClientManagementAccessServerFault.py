#
# PySNMP MIB module BW-ClientManagementAccessServerFault (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BW-ClientManagementAccessServerFault
# Produced by pysmi-0.3.4 at Wed May  1 11:42:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
recommendedActionsText, faultFields, component, common, timeStamp, alarmState, problemText, identifier, severity, subcomponent, alarmName, systemName = mibBuilder.importSymbols("BroadworksFault", "recommendedActionsText", "faultFields", "component", "common", "timeStamp", "alarmState", "problemText", "identifier", "severity", "subcomponent", "alarmName", "systemName")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Counter32, Bits, Unsigned32, ObjectIdentity, MibIdentifier, NotificationType, Integer32, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Counter32", "Bits", "Unsigned32", "ObjectIdentity", "MibIdentifier", "NotificationType", "Integer32", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
systemFaults = ModuleIdentity((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1))
systemFaults.setRevisions(('2000-09-19 14:31',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: systemFaults.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: systemFaults.setLastUpdated('200201220000Z')
if mibBuilder.loadTexts: systemFaults.setOrganization('Broadsoft, Inc')
if mibBuilder.loadTexts: systemFaults.setContactInfo('Broadsoft, Inc. 220 Perry Parkway Gaithersburg, MD 20877 301-977-9440')
if mibBuilder.loadTexts: systemFaults.setDescription('The defines the fault ')
mibBuilder.exportSymbols("BW-ClientManagementAccessServerFault", PYSNMP_MODULE_ID=systemFaults, systemFaults=systemFaults)
