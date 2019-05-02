#
# PySNMP MIB module ERICSSON-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ERICSSON-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:06:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ericssonModules, = mibBuilder.importSymbols("ERICSSON-TOP-MIB", "ericssonModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ModuleIdentity, TimeTicks, Counter64, Counter32, Unsigned32, ObjectIdentity, Integer32, NotificationType, iso, MibIdentifier, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "TimeTicks", "Counter64", "Counter32", "Unsigned32", "ObjectIdentity", "Integer32", "NotificationType", "iso", "MibIdentifier", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ericssonTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 183, 1))
ericssonTCMIB.setRevisions(('2008-10-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ericssonTCMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ericssonTCMIB.setLastUpdated('200810170000Z')
if mibBuilder.loadTexts: ericssonTCMIB.setOrganization('Ericsson AB')
if mibBuilder.loadTexts: ericssonTCMIB.setContactInfo('Email: snmp.mib.contact@ericsson.com ')
if mibBuilder.loadTexts: ericssonTCMIB.setDescription('This MIB document includes textual conventions that can be used by all of the Ericsson group. The intention is to have shared definitions such that integration and SNMP development are made easier. Document number: 2/196 03-CXC 172 7549, Rev A')
class EriMO(TextualConvention, OctetString):
    reference = '3GPP TS 32.106-8 V3.2, Name convention for Managed Objects'
    description = "The 3GPP naming convention shall be used as the format for the managed object parameter. Note that the granularity MUST be sufficient to guarantee unique alarm states and relevant resource identification to the operator. NOTE: The DN should be *relative* to the node's *own* root."
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 150)

mibBuilder.exportSymbols("ERICSSON-TC-MIB", ericssonTCMIB=ericssonTCMIB, PYSNMP_MODULE_ID=ericssonTCMIB, EriMO=EriMO)
