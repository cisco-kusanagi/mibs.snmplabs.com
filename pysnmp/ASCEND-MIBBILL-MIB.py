#
# PySNMP MIB module ASCEND-MIBBILL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBBILL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:10:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, Counter32, NotificationType, iso, Integer32, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Bits, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "Counter32", "NotificationType", "iso", "Integer32", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Bits", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibbillingProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 61))
mibbillingProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 61, 1), )
if mibBuilder.loadTexts: mibbillingProfileTable.setStatus('mandatory')
mibbillingProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 61, 1, 1), ).setIndexNames((0, "ASCEND-MIBBILL-MIB", "billingProfile-Index-o"))
if mibBuilder.loadTexts: mibbillingProfileEntry.setStatus('mandatory')
billingProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 61, 1, 1, 1), Integer32()).setLabel("billingProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: billingProfile_Index_o.setStatus('mandatory')
billingProfile_SystemDs0Minutes = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 61, 1, 1, 2), Integer32()).setLabel("billingProfile-SystemDs0Minutes").setMaxAccess("readwrite")
if mibBuilder.loadTexts: billingProfile_SystemDs0Minutes.setStatus('mandatory')
billingProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 61, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("billingProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: billingProfile_Action_o.setStatus('mandatory')
mibbillingProfile_PortDs0MinutesTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 61, 2), ).setLabel("mibbillingProfile-PortDs0MinutesTable")
if mibBuilder.loadTexts: mibbillingProfile_PortDs0MinutesTable.setStatus('mandatory')
mibbillingProfile_PortDs0MinutesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 61, 2, 1), ).setLabel("mibbillingProfile-PortDs0MinutesEntry").setIndexNames((0, "ASCEND-MIBBILL-MIB", "billingProfile-PortDs0Minutes-Index-o"), (0, "ASCEND-MIBBILL-MIB", "billingProfile-PortDs0Minutes-Index1-o"))
if mibBuilder.loadTexts: mibbillingProfile_PortDs0MinutesEntry.setStatus('mandatory')
billingProfile_PortDs0Minutes_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 61, 2, 1, 1), Integer32()).setLabel("billingProfile-PortDs0Minutes-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: billingProfile_PortDs0Minutes_Index_o.setStatus('mandatory')
billingProfile_PortDs0Minutes_Index1_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 61, 2, 1, 2), Integer32()).setLabel("billingProfile-PortDs0Minutes-Index1-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: billingProfile_PortDs0Minutes_Index1_o.setStatus('mandatory')
billingProfile_PortDs0Minutes = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 61, 2, 1, 3), Integer32()).setLabel("billingProfile-PortDs0Minutes").setMaxAccess("readwrite")
if mibBuilder.loadTexts: billingProfile_PortDs0Minutes.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBBILL-MIB", billingProfile_PortDs0Minutes=billingProfile_PortDs0Minutes, billingProfile_Index_o=billingProfile_Index_o, mibbillingProfileTable=mibbillingProfileTable, billingProfile_PortDs0Minutes_Index1_o=billingProfile_PortDs0Minutes_Index1_o, mibbillingProfileEntry=mibbillingProfileEntry, billingProfile_PortDs0Minutes_Index_o=billingProfile_PortDs0Minutes_Index_o, billingProfile_SystemDs0Minutes=billingProfile_SystemDs0Minutes, mibbillingProfile_PortDs0MinutesEntry=mibbillingProfile_PortDs0MinutesEntry, billingProfile_Action_o=billingProfile_Action_o, mibbillingProfile_PortDs0MinutesTable=mibbillingProfile_PortDs0MinutesTable, mibbillingProfile=mibbillingProfile, DisplayString=DisplayString)
