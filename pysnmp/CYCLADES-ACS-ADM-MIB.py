#
# PySNMP MIB module CYCLADES-ACS-ADM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CYCLADES-ACS-ADM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:18:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
cyACSMgmt, = mibBuilder.importSymbols("CYCLADES-ACS-MIB", "cyACSMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, Integer32, Counter32, ObjectIdentity, NotificationType, Counter64, Unsigned32, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "Integer32", "Counter32", "ObjectIdentity", "NotificationType", "Counter64", "Unsigned32", "MibIdentifier", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cyACSAdm = ModuleIdentity((1, 3, 6, 1, 4, 1, 2925, 4, 4))
cyACSAdm.setRevisions(('2005-08-29 00:00', '2002-09-20 00:00',))
if mibBuilder.loadTexts: cyACSAdm.setLastUpdated('200508290000Z')
if mibBuilder.loadTexts: cyACSAdm.setOrganization('Cyclades Corporation')
cyACSSave = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("nosave", 0), ("save", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyACSSave.setStatus('current')
cyACSSerialHUP = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("norestartportslave", 0), ("restartportslave", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyACSSerialHUP.setStatus('current')
mibBuilder.exportSymbols("CYCLADES-ACS-ADM-MIB", cyACSSerialHUP=cyACSSerialHUP, PYSNMP_MODULE_ID=cyACSAdm, cyACSAdm=cyACSAdm, cyACSSave=cyACSSave)
