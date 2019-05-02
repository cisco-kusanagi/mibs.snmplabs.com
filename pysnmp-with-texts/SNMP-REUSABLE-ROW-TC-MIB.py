#
# PySNMP MIB module SNMP-REUSABLE-ROW-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMP-REUSABLE-ROW-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:08:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, IpAddress, Counter32, Integer32, Unsigned32, Bits, MibIdentifier, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, Counter64, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Counter32", "Integer32", "Unsigned32", "Bits", "MibIdentifier", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "Counter64", "ObjectIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
snmpReusableRowTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 67890))
snmpReusableRowTCMIB.setRevisions(('2001-03-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snmpReusableRowTCMIB.setRevisionsDescriptions(('Initial version, published as RFCnnnn.',))
if mibBuilder.loadTexts: snmpReusableRowTCMIB.setLastUpdated('200103020000Z')
if mibBuilder.loadTexts: snmpReusableRowTCMIB.setOrganization('IETF Operations & Management Area')
if mibBuilder.loadTexts: snmpReusableRowTCMIB.setContactInfo('Bob Moore IBM Corporation, BRQA/502 PO Box 12195 Research Triangle Park, NC 27709, USA Phone: +1 919 254 4436 EMail: remoore@us.ibm.com Kwok Ho Chan Nortel Networks 600 Technology Park Drive Billerica, MA 01821, USA E-mail: khchan@nortelnetworks.com Send comments to mibs@ops.ietf.org.')
if mibBuilder.loadTexts: snmpReusableRowTCMIB.setDescription('This MIB module defines a textual convention that indicates whether a conceptual row is reusable.')
class ReusableRow(TextualConvention, Integer32):
    description = "This textual convention characerizes a conceptual row as reusable or not reusable for the purposes of cloning a configuration template. The objects being cloned may either be special ones that express configuration information at the mechanism-specific level, or simply instance-specific ones that already exist at the time the cloning is done. The following values are defined: - other(1) - reusable(2): the conceptual row is available to be pointed to by mulitple RowPointer objects. - singleUse(3): a separate copy of the conceptual row is needed for each RowPointer object that points to it. Because it represents a capability of the managed sytsem, rather than something that is configurable, an object having this syntax SHOULD have MAX-ACCESS of 'read-only'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("reusable", 2), ("singleUse", 3))

mibBuilder.exportSymbols("SNMP-REUSABLE-ROW-TC-MIB", ReusableRow=ReusableRow, snmpReusableRowTCMIB=snmpReusableRowTCMIB, PYSNMP_MODULE_ID=snmpReusableRowTCMIB)
