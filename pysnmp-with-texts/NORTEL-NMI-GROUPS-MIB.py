#
# PySNMP MIB module NORTEL-NMI-GROUPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NORTEL-NMI-GROUPS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:23:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
nortelNMIconformanceMIBs, = mibBuilder.importSymbols("NORTEL-NMI-CONFORMANCE-MIB", "nortelNMIconformanceMIBs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Bits, iso, IpAddress, Integer32, Gauge32, TimeTicks, ObjectIdentity, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "iso", "IpAddress", "Integer32", "Gauge32", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nortelNMImibGroups = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1, 2, 1))
nortelNMImibGroups.setRevisions(('1999-06-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: nortelNMImibGroups.setRevisionsDescriptions((' The first version of this MIB module. Revisions introduced by Shobana Sundaram.',))
if mibBuilder.loadTexts: nortelNMImibGroups.setLastUpdated('9906240000Z')
if mibBuilder.loadTexts: nortelNMImibGroups.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: nortelNMImibGroups.setContactInfo(' Jingdong Liu Postal: Nortel Networks P. O. Box 3511, Station C Ottawa, Ontario CANADA K1Y 4H7 Email: jingdong@nortelnetworks.com')
if mibBuilder.loadTexts: nortelNMImibGroups.setDescription('This module contains the object group definitions for the Network Management Interface (NMI) MIBs. ')
nortelNMIobjectGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1, 2, 1, 1))
if mibBuilder.loadTexts: nortelNMIobjectGroups.setStatus('current')
if mibBuilder.loadTexts: nortelNMIobjectGroups.setDescription('This OID represents the branch for the object group definitions.')
nortelNMInotificationGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1, 2, 1, 2))
if mibBuilder.loadTexts: nortelNMInotificationGroups.setStatus('current')
if mibBuilder.loadTexts: nortelNMInotificationGroups.setDescription('This OID represents the branch for the notification group definitions.')
mibBuilder.exportSymbols("NORTEL-NMI-GROUPS-MIB", nortelNMInotificationGroups=nortelNMInotificationGroups, nortelNMIobjectGroups=nortelNMIobjectGroups, PYSNMP_MODULE_ID=nortelNMImibGroups, nortelNMImibGroups=nortelNMImibGroups)
