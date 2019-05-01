#
# PySNMP MIB module CISCO-DMN-DSG-SESSIONCONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-SESSIONCONTROL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:55:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, ModuleIdentity, Counter64, Gauge32, NotificationType, ObjectIdentity, Unsigned32, IpAddress, MibIdentifier, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "ModuleIdentity", "Counter64", "Gauge32", "NotificationType", "ObjectIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "iso", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGSessionControl = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6))
ciscoDSGSessionControl.setRevisions(('2010-08-30 11:00', '2009-11-22 15:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGSessionControl.setRevisionsDescriptions(('V01.00.01 2010-08-30 Updated for adherence to SNMPv2 format.', 'V01.00.00 2009-11-22 Initial Version.',))
if mibBuilder.loadTexts: ciscoDSGSessionControl.setLastUpdated('201008301100Z')
if mibBuilder.loadTexts: ciscoDSGSessionControl.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGSessionControl.setContactInfo('Cisco Systems, Inc. Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 NETS E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGSessionControl.setDescription('Cisco DSG Session Control MIB.')
sessionControlOpen = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("open", 1), ("writeOnly", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sessionControlOpen.setStatus('current')
if mibBuilder.loadTexts: sessionControlOpen.setDescription('Open the session. 1 indicates OPEN.')
sessionControlClose = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("saveAndClose", 1), ("ignoreAndClose", 2), ("writeOnly", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sessionControlClose.setStatus('current')
if mibBuilder.loadTexts: sessionControlClose.setDescription('Close the session.')
sessionControlStatus = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("open", 1), ("closed", 2), ("expired", 3), ("openWithInvalidConfig", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sessionControlStatus.setStatus('current')
if mibBuilder.loadTexts: sessionControlStatus.setDescription('Status of the last opened session.')
sessionControlValidateStatus = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 250))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sessionControlValidateStatus.setStatus('current')
if mibBuilder.loadTexts: sessionControlValidateStatus.setDescription('If the sessioncontrolstatus object displays invalid configuration, this object displays the reason for invalidity.')
mibBuilder.exportSymbols("CISCO-DMN-DSG-SESSIONCONTROL-MIB", sessionControlClose=sessionControlClose, sessionControlStatus=sessionControlStatus, sessionControlOpen=sessionControlOpen, ciscoDSGSessionControl=ciscoDSGSessionControl, PYSNMP_MODULE_ID=ciscoDSGSessionControl, sessionControlValidateStatus=sessionControlValidateStatus)
